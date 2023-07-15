# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest pitstop.json

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

pit_stops_schema = StructType(fields = [StructField("raceId",IntegerType(),False),
                                      StructField("driverId",IntegerType(),True),
                                      StructField("stop",StringType(),True),
                                      StructField("lag",IntegerType(),True), 
                                      StructField("time",StringType(),True),  
                                      StructField("duration",StringType(),True),
                                      StructField("milliseconds",IntegerType(),True)
])

# COMMAND ----------

# re-read the data in the correct format
pit_stop_df = spark.read \
.schema(pit_stops_schema) \
.option("multiline",True) \
.json(f"{raw_folder_path}/{v_as_of_date}/pit_stops.json")

# COMMAND ----------

display(pit_stop_df)

# COMMAND ----------

pit_stop_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit
pit_stop_final = pit_stop_df.withColumnRenamed("raceId","race_id") \
                            .withColumnRenamed("driverId","driver_id") \
                            .withColumn("data_source",lit(v_data_source)) \
                            .withColumn("as_of_date",lit(v_as_of_date))                        

# COMMAND ----------

pit_stop_final = add_ingestion_date(pit_stop_final)

# COMMAND ----------

display(pit_stop_final)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the form of the parquet files

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python but no table creation

# COMMAND ----------

# full load with file creation.
# pit_stop_final.write.mode("overwrite").partitionBy('race_id').parquet(f"{processed_folder_path}/pit_stops")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Data Lake + Table Creation

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# full load with table and file creation.
#
pit_stop_final.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("processed_db.pit_stops")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Delta Lake + Table Creation 

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# pit_stop_final.write.mode("overwrite").format("delta").saveAsTable("processed_db.pit_stops")

# COMMAND ----------

# MAGIC %md
# MAGIC ## READ the Solution 1 and Solution 2 from the "injection/5.ingest_results_file.json"
# MAGIC ## Here Solution 2 with function is implemented

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
# overwrite_partition_data(pit_stop_final,'processed_db','pit_stops','race_id')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

## I choosen the wrong primary key and some data can be duplicate
# input_db="processed_db"
# input_table="pit_stops"
# partition_id="race_id"
# primary_key="driver_id"
# merge_delta_data(pit_stop_final,input_db,input_table,processed_folder_path,partition_id,primary_key)

# COMMAND ----------

# %sql
# select as_of_date,count(*) from processed_db.pit_stops group by as_of_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python read

# COMMAND ----------

# df = spark.read.parquet(f"{processed_folder_path}/pit_stops")
# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

df = spark.read.parquet(f"{processed_folder_path}/pit_stops")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
# df = spark.read.format("delta").load(f"{processed_folder_path}/pit_stops")
# display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")
