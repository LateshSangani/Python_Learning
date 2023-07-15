# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest results.json

# COMMAND ----------

# Include the common files to export the common variable and functions.
# The filename without extention is fine
# "/Repos/sangani.sangita@gmail.com/Python_Learning/formula1/include/configuration"
# "/Repos/sangani.sangita@gmail.com/Python_Learning/formula1/include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All Initial configuration files

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All the Widgets

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
dbutils.widgets.text("p_data_source","")
v_data_source = dbutils.widgets.get("p_data_source")
display(v_data_source)


# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is 2099-01-01  , but it can be anything we defined.
dbutils.widgets.text("p_as_of_date","2099-01-01")
v_as_of_date = dbutils.widgets.get("p_as_of_date")
display(v_as_of_date)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1 : Read the JSON file

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, IntegerType , StringType , DateType , FloatType

# COMMAND ----------

results_schema = StructType(fields = [StructField("resultId",IntegerType(),False),
                                      StructField("raceId",IntegerType(),True),
                                      StructField("driverId",IntegerType(),True),
                                      StructField("constructorId",IntegerType(),True),
                                      StructField("number",IntegerType(),True), 
                                      StructField("grid",IntegerType(),True),  
                                      StructField("position",IntegerType(),True),
                                      StructField("positionText",StringType(),True),
                                      StructField("positionOrder",IntegerType(),True),
                                      StructField("points",FloatType(),True),
                                      StructField("laps",IntegerType(),True),
                                      StructField("time",StringType(),True),
                                      StructField("milliseconds",IntegerType(),True),
                                      StructField("fastestLap",IntegerType(),True),
                                      StructField("rank",IntegerType(),True),
                                      StructField("fastestLapTime",StringType(),True),
                                      StructField("fastestLapSpeed",StringType(),True),
                                      StructField("statusId",IntegerType(),True)
])

# COMMAND ----------

results_df = spark.read \
.schema(results_schema) \
.json(f"{raw_folder_path}/{v_as_of_date}/results.json")

# COMMAND ----------

display(results_df)

# COMMAND ----------

#results_df.schema.names
results_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit
results_final_df = results_df.withColumnRenamed("resultId","result_id") \
                            .withColumnRenamed("raceId","race_id") \
                            .withColumnRenamed("driverId","driver_id") \
                            .withColumnRenamed("constructorId","constructor_id") \
                            .withColumnRenamed("positionText","position_text") \
                            .withColumnRenamed("positionOrder","position_order") \
                            .withColumnRenamed("fastestLap","fastest_lap") \
                            .withColumnRenamed("fastestLapTime","fastest_lap_time") \
                            .withColumnRenamed("fastestLapSpeed","fastest_lap_speed") \
                            .withColumn("data_source",lit(v_data_source)) \
                            .withColumn("as_of_date",lit(v_as_of_date)) \
                            .drop(col("statusId"))

# COMMAND ----------

results_final_df = add_ingestion_date(results_final_df)

# COMMAND ----------

# remove the duplicate data

# COMMAND ----------

results_final_df = results_final_df.dropDuplicates(["race_id","driver_id"])

# COMMAND ----------

display(results_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the form of the parquet files

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python but no table creation

# COMMAND ----------

# full load with file creation.
# results_final_df.write.mode("overwrite").partitionBy("race_id").parquet(f"{processed_folder_path}/results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Data Lake + Table Creation

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# full load with table and file creation.
results_final_df.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("processed_db.results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Delta Lake + Table Creation 

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# results_final_df.write.mode("overwrite").format("delta").saveAsTable("processed_db.results")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Note : While running code with solution 1 or solution 2 : comment any one solution both does not required to run together
# MAGIC ### Note : Solution 2 with FUNCTION use is most sopisticated and re-usable code for the production code

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 1 : Incremental laod ( append )  Simple but Slow Performance
# MAGIC ### For the incremenal write with append option is not re-runnable. it will add duplicate values in the table
# MAGIC ### The partition has to drop in the loop before insert and check the table is present and any old partition made on it.

# COMMAND ----------

# MAGIC %md
# MAGIC ##### In databricks with spark sql or plain SQL their is no feature of the DELETE or TRUNCATE.
# MAGIC ##### Spark SQL support the DROP TABLE in the sql cell

# COMMAND ----------

#for race_id_list in results_final_df.select("race_id").distinct().collect():
#    if (spark._jsparkSession.catalog().tableExists("processed_db.results")):
#        print(race_id_list.race_id)
#        spark.sql(f"ALTER TABLE processed_db.results DROP IF EXISTS PARTITION ( race_id = {race_id_list.race_id} )")

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# results_final_df.write.mode("append").partitionBy('race_id').format("parquet").saveAsTable("processed_db.results")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 2 : Incremental laod ( overwrite ) Complex but Fast Performance
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

# this tell to spark that while running the insertInto if Paration already exists then replace the VALUES only with new values coming from the dataframe.
# So here we are not deleting the partition like we did in the Solution 1

# spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")

# COMMAND ----------

# For this solution 2 the partition column race_id should be at LAST
#
# results_final_df = results_final_df.select("result_id","driver_id","constructor_id","number","grid","position","position_text","position_order","points","laps","time","milliseconds","fastest_lap","rank","fastest_lap_time","fastest_lap_speed","data_source","as_of_date","ingestion_date","race_id")

# COMMAND ----------

# for the first time load the ELSE part will execute , later for all the incremental load the IF (Inset) will work
# The question comes if same incremental load again then it will again go in the IF statment and insert the new data.
# The solution is               spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
# this tell to spark that while running the insertInto if Paration already exists then replace the VALUES only with new values coming from the dataframe.
# So here we are not deleting the partition like we did in the Solution 1
#
#if (spark._jsparkSession.catalog().tableExists("processed_db.results")):
#    results_final_df.write.mode("overwrite").insertInto("processed_db.results")
#else:
#    results_final_df.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("processed_db.results")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 2 (Enhancement): Incremental laod ( overwrite ) Complex but Fast Performance (USE FUNCTIONS)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

# MAGIC %md
# MAGIC ### signiture of the functions
# MAGIC ### CHILD : append_column(input_df,partition_id)    Output : output_df
# MAGIC ### PARENT : overwrite_partition_data(input_df,input_db,input_table,partition_id) Output : output_df

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
# overwrite_partition_data(results_final_df,'processed_db','results','race_id')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

#input_db="processed_db"
#input_table="results"
#partition_id="race_id"
#primary_key="result_id"
#merge_delta_data(results_final_df,input_db,input_table,processed_folder_path,partition_id,primary_key)

# COMMAND ----------

# %sql
# select as_of_date,count(*) from processed_db.results group by as_of_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Check the duplicate data issue

# COMMAND ----------

# %sql
# select race_id,driver_id,count(*) from processed_db.results group by race_id,driver_id having count(*) > 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python read

# COMMAND ----------

 # df = spark.read.parquet(f"{processed_folder_path}/results")
 # display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

 df = spark.read.parquet(f"{processed_folder_path}/results")
 display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
# df = spark.read.format("delta").load(f"{processed_folder_path}/results")
# display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")
