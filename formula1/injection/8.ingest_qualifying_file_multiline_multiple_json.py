# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest qualiying 

# COMMAND ----------

# Include the common files to export the common variable and functions.
# The filename without extention is fine
# "/formula1/include/configuration"
# "/formula1/include/common_functions"

# COMMAND ----------

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
# MAGIC ## Step 1 : Read the multiple json file and each file has multiple lines

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, IntegerType , StringType , DateType , FloatType

# COMMAND ----------

qualifying_schema = StructType(fields = [StructField("qualifyId",IntegerType(),False),
                                      StructField("raceId",IntegerType(),True),
                                      StructField("driverId",IntegerType(),True),
                                      StructField("constructorId",IntegerType(),True), 
                                      StructField("number",IntegerType(),True),  
                                      StructField("position",IntegerType(),True),
                                      StructField("q1",StringType(),True),
                                      StructField("q2",StringType(),True),
                                      StructField("q3",StringType(),True),
])

# COMMAND ----------

# Providing the full folder only and no file name pattern will also work but condition is that all the files has same structure.
qualifying_df = spark.read \
.schema(qualifying_schema) \
.option("multiline",True) \
.json(f"{raw_folder_path}/{v_as_of_date}/qualifying/qualifying_split_*.json")

# COMMAND ----------

# By default spark only read the single list either JSON or CSV file.
# Here all the colummns values are coming null
display(qualifying_df)

# COMMAND ----------

# check the count as data is disturbuted in the multiple files
qualifying_df.count()

# COMMAND ----------

qualifying_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit
qualifying_final = qualifying_df.withColumnRenamed("qualifyId","qualify_id") \
                            .withColumnRenamed("raceId","race_id") \
                            .withColumnRenamed("driverId","driver_id") \
                            .withColumnRenamed("constructorId","constructor_id") \
                            .withColumn("data_source",lit(v_data_source)) \
                            .withColumn("as_of_date",lit(v_as_of_date))

# COMMAND ----------

qualifying_final = add_ingestion_date(qualifying_final)

# COMMAND ----------

display(qualifying_final)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the form of the parquet files

# COMMAND ----------

# full load with file creation.
#
# qualifying_final.write.mode("overwrite").partitionBy('race_id').parquet(f"{processed_folder_path}/qualifying")

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# full load with table and file creation.
#
# qualifying_final.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("processed_db.qualifying")

# COMMAND ----------

# MAGIC %md
# MAGIC ## READ the Solution 1 and Solution 2 from the "injection/5.ingest_results_file.json"
# MAGIC ## Here Solution 2 with function is implemented

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
# overwrite_partition_data(qualifying_final,'processed_db','qualifying','race_id')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

input_db="processed_db"
input_table="qualifying"
partition_id="race_id"
primary_key="qualify_id"
merge_delta_data(qualifying_final,input_db,input_table,processed_folder_path,partition_id,primary_key)

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.qualifying group by as_of_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

# df = spark.read.parquet(f"{processed_folder_path}/qualifying")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.format("delta").load(f"{processed_folder_path}/qualifying")

# COMMAND ----------

display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")