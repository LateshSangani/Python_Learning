# Databricks notebook source
# MAGIC %md
# MAGIC ## Ingest races.csv file

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
# MAGIC ## Step1 : Read CSV file using the Spark Data frame reader

# COMMAND ----------

#The above dispaly is not good , hence use the display function to get the better display in table format.
display(dbutils.fs.mounts())

# COMMAND ----------

# The alternative of the interSchema is to make own schema and use while reading it.
# the Struct is required to prepared, For that import Struct
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DoubleType,DateType

# COMMAND ----------

# StructField("column_name","datatype",NULL/NOT NULL)
# False is NOT NULL
# True is NULL
# StructType --> represent rows
# StructField --> represent columns
races_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                     StructField("year", IntegerType(), True),
                                     StructField("round", IntegerType(), True),
                                     StructField("circuitId", IntegerType(), True),
                                     StructField("name", StringType(), True),
                                     StructField("date", DateType(), True),
                                     StructField("time", StringType(), True),
                                     StructField("url", StringType(), True)
])

# COMMAND ----------

# use the circuits_schema while reading the dataframe from the CSV file.
races_df = spark.read \
.option("header" ,True) \
.schema(races_schema) \
.csv(f"{raw_folder_path}/{v_as_of_date}/races.csv")

# COMMAND ----------

display(races_df)

# COMMAND ----------

#races_df.schema.names
races_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

# the extra column is added with name ingestion_date and it holds the current timestamp values.
from pyspark.sql.functions import current_timestamp,to_timestamp,concat,lit,col
races_final_df = races_df \
.withColumnRenamed("raceId","race_id") \
.withColumnRenamed("year","race_year") \
.withColumnRenamed("circuitId","circuit_id") \
.withColumn("race_timestamp",to_timestamp(concat(col('date'),lit(' '),col('time')), 'yyyy-MM-dd HH:mm:ss')) \
.withColumn("ingestion_date",current_timestamp()) \
.withColumn("data_source",lit(v_data_source)) \
.withColumn("as_of_date",lit(v_as_of_date))

# COMMAND ----------

races_final_df = races_final_df \
.drop("date") \
.drop("time") \
.drop("url")

# COMMAND ----------

races_final_df = add_ingestion_date(races_final_df)

# COMMAND ----------

display(races_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the database using the parqut format
# MAGIC #### Make the partition on race_year column for the parallel processing of the cluster

# COMMAND ----------

# Re-running the entire note book fails the write statement has path already present
# add the mode option to overwrite the new existing file
# races_final_df.write.mode("overwrite").partitionBy("race_year").parquet(f"{processed_folder_path}/races")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### full load with data lake

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# races_final_df.write.mode("overwrite").partitionBy('race_year').format("parquet").saveAsTable("processed_db.races")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### full load with delta lake

# COMMAND ----------

races_final_df.write.mode("overwrite").partitionBy('race_year').format("delta").saveAsTable("processed_db.races")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

# df = spark.read.parquet(f"{processed_folder_path}/races")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# confirm the data is stored well and read all the files
df = spark.read.format("delta").load(f"{processed_folder_path}/races")

# COMMAND ----------

display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")