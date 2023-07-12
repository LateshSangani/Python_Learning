# Databricks notebook source
# MAGIC %md 
# MAGIC ## Load All Initial configuration files

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All the Widgets

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is 2099-01-01  , but it can be anything we defined.
dbutils.widgets.text("p_as_of_date","2099-01-01")
v_as_of_date = dbutils.widgets.get("p_as_of_date")
display(v_as_of_date)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create the Empty Database

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS demo
# MAGIC LOCATION '/mnt/databrickscourcedl/demo';

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/databrickscourcedl/demo

# COMMAND ----------

results_df = spark.read \
.option("inferSchema", True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/results.json")

# COMMAND ----------

# MAGIC %md
# MAGIC #                                                                    Data Lake Approch
# MAGIC #
# MAGIC ### WRITE : Way to write the files in storage location
# MAGIC ##### results_df.write.mode("overwrite").partitionBy("race_id").parquet(f"{processed_folder_path}/results")
# MAGIC #
# MAGIC ### WRITE : Way to write the files in the table
# MAGIC ##### results_df.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("processed_db.results")
# MAGIC #
# MAGIC ### READ : Way to read the files from the storage location
# MAGIC ##### results_df = spark.read.parquet(f"{processed_folder_path}/results/")
# MAGIC #
# MAGIC ### READ : Way to read the files from the table
# MAGIC ##### select * from processed_db.results

# COMMAND ----------

# MAGIC %md
# MAGIC # Delta Lake Approch  ( DML OPERATIONS)

# COMMAND ----------

# MAGIC %md
# MAGIC ## INSERT : DELTA Way to store in the form of the FILES

# COMMAND ----------

# save the flat files
# mode can be overwrite or append
# format parquet replaced by delta
results_df = spark.read \
.option("inferSchema", True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/results.json")

results_df.write.mode("overwrite").format("delta").save("/mnt/databrickscourcedl/demo/results_external")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/databrickscourcedl/demo/results_external

# COMMAND ----------

# MAGIC %md
# MAGIC ## SELECT : DELTA Way to READ from the FILES

# COMMAND ----------

result_df = spark.read.format("delta").load("/mnt/databrickscourcedl/demo/results_external")
result_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## INSERT : DELTA Way to store in the form of the MANAGED TABLE

# COMMAND ----------

# save the data in the form of the table.
# mode can be overwrite or append
# format parquet replaced by delta
results_df = spark.read \
.option("inferSchema", True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/results.json")

results_df.write.mode("overwrite").partitionBy("raceId").format("delta").saveAsTable("demo.results_managed")

# COMMAND ----------

# MAGIC %md
# MAGIC ## SELECT : DELTA Way to read data from the MANAGED TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.results_managed;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW PARTITIONS demo.results_managed;

# COMMAND ----------

# MAGIC %md
# MAGIC ## INSERT : DELTA Way to store in the form of the EXTERNAL TABLE

# COMMAND ----------

results_df = spark.read \
.option("inferSchema", True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/results.json")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE demo.results_external
# MAGIC USING DELTA
# MAGIC LOCATION "/mnt/databrickscourcedl/demo/results_external"

# COMMAND ----------

# MAGIC %md
# MAGIC ## SELECT : DELTA Way to READ read the data from the EXTERNAL TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.results_external;

# COMMAND ----------

# MAGIC %md
# MAGIC ## UPDATE : DELTA Way to UPDATE of the MANAGED TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE demo.results_managed
# MAGIC SET POINTS = 11-POSITION
# MAGIC WHERE POSITION <= 10;
# MAGIC 
# MAGIC SELECT * FROM demo.results_managed WHERE POSITION <= 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## UPDATE : DELTA Way to UPDATE of the FILES

# COMMAND ----------

# NOTE : The file is being updated here is the part of the TABLE only , just this is Python Way
from delta.tables import DeltaTable
deleteTable = DeltaTable.forPath(spark,"/mnt/databrickscourcedl/demo/results_managed/")
deleteTable.update( "POSITION <= 10",{"POINTS" : "21-POSITION"} )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.results_managed WHERE POSITION <= 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELETE : DELTA Way for DELETE of the MANAGED TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(1) from demo.results_managed;  --before delete

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from demo.results_managed WHERE POSITION >= 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(1) from demo.results_managed; --after delete

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELETE : DELTA Way for DELETE from the files

# COMMAND ----------

# NOTE : The file is being updated here is the part of the TABLE only , just this is Python Way
from delta.tables import DeltaTable
deleteTable = DeltaTable.forPath(spark,"/mnt/databrickscourcedl/demo/results_managed/")
deleteTable.delete( "POINTS <= 0" )

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(1) from demo.results_managed; --after delete

# COMMAND ----------

# MAGIC %md
# MAGIC ## MERGE : DELTA Way for MERGE of the MANAGED TABLE

# COMMAND ----------

# MAGIC %md
# MAGIC ### Big scenerio is prepared to test the results

# COMMAND ----------

# MAGIC %md
# MAGIC ## DAY 1 Data

# COMMAND ----------

# Read half and partial data for TESTING purpose of the Merge opetion to add or update data.
drivers_day1_df = spark.read \
.option("inferSchema",True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/drivers.json") \
.filter("driverId <= 10") \
.select("driverId","dob","name.forename","name.surname")

drivers_day1_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### temp table for the sql operation

# COMMAND ----------

drivers_day1_df.createOrReplaceTempView("drivers_day1")

# COMMAND ----------

# MAGIC %md
# MAGIC ## DAY 2 Data

# COMMAND ----------

from pyspark.sql.functions import  upper
drivers_day2_df = spark.read \
.option("inferSchema",True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/drivers.json") \
.filter("driverId BETWEEN 6 AND 15") \
.select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

drivers_day2_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### temp table for the sql operation

# COMMAND ----------

drivers_day2_df.createOrReplaceTempView("drivers_day2")

# COMMAND ----------

# MAGIC %md
# MAGIC ## DAY 3 Data

# COMMAND ----------

drivers_day3_df = spark.read \
.option("inferSchema",True) \
.json("/mnt/databrickscourcedl/raw/2021-03-28/drivers.json") \
.filter("driverId BETWEEN 1 AND 5 OR driverId BETWEEN 16 AND 20") \
.select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

drivers_day3_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### temp table for the sql operation

# COMMAND ----------

drivers_day3_df.createOrReplaceTempView("drivers_day3")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Main DELTA Table to Collect all the three days data

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS demo.drivers_merge (
# MAGIC driverId INT,
# MAGIC dob DATE,
# MAGIC forename STRING,
# MAGIC surname STRING,
# MAGIC creationDate DATE,
# MAGIC updatedDate DATE
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %md
# MAGIC ## merge operation for the day 1 data

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO demo.drivers_merge target     --  < 10
# MAGIC USING drivers_day1 upd
# MAGIC ON target.driverId = upd.driverId
# MAGIC WHEN MATCHED THEN 
# MAGIC UPDATE SET target.dob = upd.dob,
# MAGIC target.forename = upd.forename,
# MAGIC target.surname = upd.surname,
# MAGIC target.updatedDate = current_timestamp
# MAGIC WHEN NOT MATCHED
# MAGIC THEN INSERT (driverId,dob,forename,surname,creationDate) VALUES (driverId,dob,forename,surname,current_timestamp)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_merge;

# COMMAND ----------

# MAGIC %md
# MAGIC ## merge operation for the day 2 data

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO demo.drivers_merge target  --BETWEEN 6 AND 15
# MAGIC USING drivers_day2 upd
# MAGIC ON target.driverId = upd.driverId
# MAGIC WHEN MATCHED THEN 
# MAGIC UPDATE SET target.dob = upd.dob,
# MAGIC target.forename = upd.forename,
# MAGIC target.surname = upd.surname,
# MAGIC target.updatedDate = current_timestamp
# MAGIC WHEN NOT MATCHED
# MAGIC THEN INSERT (driverId,dob,forename,surname,creationDate) VALUES (driverId,dob,forename,surname,current_timestamp)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_merge;

# COMMAND ----------

# MAGIC %md
# MAGIC ## MERGE : DELTA Way for MERGE of the FILES

# COMMAND ----------

# MAGIC %md
# MAGIC ## merge operation for the day 3 data

# COMMAND ----------

#driverId BETWEEN 1 AND 5 OR driverId BETWEEN 16 AND 20
from delta.tables import DeltaTable
deltaTable = DeltaTable.forPath(spark,"/mnt/databrickscourcedl/demo/drivers_merge/")

deltaTable.alias("target").merge(drivers_day3_df.alias("upd"),"target.driverId = upd.driverId") \
.whenMatchedUpdate(set = {"dob" : "upd.dob" , "forename" : "upd.forename" , "surname" : "upd.surname" , "updatedDate" : "current_timestamp()" } ) \
.whenNotMatchedInsert(values =
  {
      "driverId" : "upd.driverId",
      "dob" : "upd.dob",
      "forename" : "upd.forename",
      "surname" : "upd.surname",
      "creationDate" : "current_timestamp()"
  }
) \
.execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_merge

# COMMAND ----------

# MAGIC %md
# MAGIC ## History of the DELTA tables  using VERSION

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_merge;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.drivers_merge VERSION AS OF 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.drivers_merge VERSION AS OF 4;

# COMMAND ----------

# MAGIC %md
# MAGIC ## History of the DELTA tables  using TIMESTAMP

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.drivers_merge TIMESTAMP AS OF "2022-12-26T11:03:48.000+0000";  --version 1 timestamp data

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.drivers_merge TIMESTAMP AS OF "2022-12-26T11:37:33.000+0000";  --version 4 timestamp data

# COMMAND ----------

# version 1 timestamp
df = spark.read.format("delta").option("timestampAsOf", "2022-12-26T11:03:48.000+0000").load("/mnt/databrickscourcedl/demo/drivers_merge/")
df.display()

# COMMAND ----------

# version 4 timestamp
df = spark.read.format("delta").option("timestampAsOf", "2022-12-26T11:37:33.000+0000").load("/mnt/databrickscourcedl/demo/drivers_merge/")
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELETE History of the Old data ( VACUUM )
# MAGIC ##### See delete will also make the entry in the history and that history can again read, so even data is deleted from the main table but it can be read from the history

# COMMAND ----------

# MAGIC %md
# MAGIC ##### by default the vacuum delete less than 7 days of the data

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM demo.drivers.merge;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### setting vaccum with RETAIN 0 HOURS

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM demo.drivers.merge RETAIN 0 HOURS;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### force to overwrite the vacuum 168 hours policy

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false;
# MAGIC VACUUM demo.drivers.merge RETAIN 0 HOURS;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### the vacuum deleted the all the history of the data but the current data will still present
# MAGIC ##### we can see the past history logs but now we cannot see the data in the select querry VERSION clause

# COMMAND ----------

select * from demo.drivers.merge;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### error while reading the history

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM demo.drivers_merge TIMESTAMP AS OF "2022-12-26T11:03:48.000+0000";  --version 1 timestamp data

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_merge;

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELETE BY MISTAKE RECORDS RECOVERY
# MAGIC ##### copy the data from the previous version in the current version using the MERGE statment

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from demo.drivers_merge where driverId = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO demo.drivers_merge target
# MAGIC USING target.drivers_merge VERSION AS OF 4 source
# MAGIC ON (target.driverId = source.driverId)
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_merge where driverId = 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_merge

# COMMAND ----------

# MAGIC %md
# MAGIC ## TRANSACTIONS ON Delta Lake

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS demo.drivers_txn (
# MAGIC driverId INT,
# MAGIC dob DATE,
# MAGIC forename STRING,
# MAGIC surname STRING,
# MAGIC creationDate DATE,
# MAGIC updatedDate DATE
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %md
# MAGIC ####  this create table has prepared the new folder inside of the azure gene2 storage account
# MAGIC ####  databrickscourcedl/demo/drivers_txn/_delta_log  , this folder holds all the HISTORY And Version information.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_txn

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.drivers_txn   --insert some test data to see the modify _delta_log
# MAGIC SELECT * FROM demo.drivers_merge
# MAGIC WHERE driverId in (2,3);
# MAGIC SELECT * FROM demo.drivers_txn;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_txn

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO demo.drivers_txn   --insert some test data to see the modify _delta_log
# MAGIC SELECT * FROM demo.drivers_merge
# MAGIC WHERE driverId in (4,5);
# MAGIC SELECT * FROM demo.drivers_txn;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_txn

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from demo.drivers_txn 
# MAGIC WHERE driverId in (4,5);

# COMMAND ----------

# MAGIC %sql
# MAGIC DESC HISTORY demo.drivers_txn

# COMMAND ----------

# MAGIC %md
# MAGIC ### expriment to test that each version increment to add the more number of the parquet files in the storage folder.
# MAGIC ### this will take also the backup copy from in the _delta_log folders.

# COMMAND ----------

for i in range(5,15):
    spark.sql(f""" insert into demo.drivers_txn select * from demo.drivers_merge where driverId = {i} """)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_txn

# COMMAND ----------

# MAGIC %md
# MAGIC ## Convert the Parquet table into Delta table ( As some projects has existing parquet table and like to convert from data lake to delta lake)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS demo.drivers_parquet (
# MAGIC driverId INT,
# MAGIC dob DATE,
# MAGIC forename STRING,
# MAGIC surname STRING,
# MAGIC creationDate DATE,
# MAGIC updatedDate DATE
# MAGIC )
# MAGIC USING PARQUET;

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into demo.drivers_parquet
# MAGIC select * from demo.drivers_merge;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo.drivers_parquet;

# COMMAND ----------

# MAGIC %sql
# MAGIC CONVERT TO DELTA demo.drivers_parquet;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Convert the Parquet file into Delta files ( As some projects has existing parquet files  and like to convert from parquet to delta files)

# COMMAND ----------

# both spark.table("demo.drivers_parquet")   and   spark.sql("select * from demo.drivers_parquet")  are same.
#df = spark.table("demo.drivers_parquet")
df = spark.sql("select * from demo.drivers_parquet")
df.display()

# COMMAND ----------

# prepare the sample parquet file to make delta files
df.write.format("parquet").save("/mnt/databrickscourcedl/demo/parquet_files")

# COMMAND ----------

# MAGIC %sql
# MAGIC CONVERT TO DELTA parquet.`/mnt/databrickscourcedl/demo/parquet_files`;   --NOTE : Here tick symbol is used not the single quote.

# COMMAND ----------
