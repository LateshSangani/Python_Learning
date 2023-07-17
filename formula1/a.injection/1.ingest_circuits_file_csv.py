# Databricks notebook source
# MAGIC %md
# MAGIC ## Ingest circuites.csv file

# COMMAND ----------

# Include the common file to export the common variable and functions.
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
# the default value is ""  , but it can be anything we defined.
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
# MAGIC ## Step 1 : Read CSV file using the Spark Data frame reader

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# The alternative of the interSchema is to make own schema and use while reading it.
# the Struct is required to prepared, For that import Struct
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DoubleType

# COMMAND ----------

# StructField("column_name","datatype",NULL/NOT NULL)
# False is NOT NULL
# True is NULL
# StructType --> represent rows
# StructField --> represent columns
circuits_schema = StructType(fields=[StructField("circuitId", IntegerType(), False),
                                     StructField("circuitRef", StringType(), True),
                                     StructField("name", StringType(), True),
                                     StructField("location", StringType(), True),
                                     StructField("country", StringType(), True),
                                     StructField("lat", DoubleType(), True),
                                     StructField("lng", DoubleType(), True),
                                     StructField("alt", IntegerType(), True),
                                     StructField("url", StringType(), True)
])

# COMMAND ----------

# use the circuits_schema while reading the dataframe from the CSV file.
# By default the header is set to false and spark consider the header has data record. The True skip the header 1st record.
# If schema is not assigned by default all the rows will be consider the string. hence STRUCT gives the valid data type defination
circuits_df = spark.read \
.option("header" ,True) \
.schema(circuits_schema) \
.csv(f"{raw_folder_path}/{v_as_of_date}/circuits.csv")

# COMMAND ----------

#circuits_df.show()  poor display 
display(circuits_df)

# COMMAND ----------

#circuits_df.schema.names
circuits_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

# The lit function is required to convert the variable in the form of the column
from pyspark.sql.functions import lit
circuites_final_df = circuits_df.withColumnRenamed("circuitId","circuit_id") \
.withColumnRenamed("circuitRef","circuit_ref") \
.withColumnRenamed("lat","latitude") \
.withColumnRenamed("lng","longitude") \
.withColumnRenamed("alt","altitude") \
.drop("url") \
.withColumn("data_source",lit(v_data_source)) \
.withColumn("as_of_date",lit(v_as_of_date))

# COMMAND ----------

display(circuites_final_df)

# COMMAND ----------

# the extra column is added with name ingestion_date and it holds the current timestamp values.
from pyspark.sql.functions import current_timestamp
#add the new column with full command
#circuites_final_df = circuites_final_df.withColumn("ingestion_date",current_timestamp())
#add the new column with function imported
circuites_final_df = add_ingestion_date(circuites_final_df)

# COMMAND ----------

display(circuites_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the database using the parquet format

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python but no table creation

# COMMAND ----------

# Re-running the entire note book fails the write statement has path already present
# add the mode option to overwrite the existing file
# circuites_final_df.write.mode("overwrite").parquet(f"{processed_folder_path}/circuits/")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Data Lake + Table Creation

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# circuites_final_df.write.mode("overwrite").format("parquet").saveAsTable("processed_db.circuits")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Delta Lake + Table Creation 

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
circuites_final_df.write.mode("overwrite").format("delta").saveAsTable("processed_db.circuits")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python read

# COMMAND ----------

# df = spark.read.parquet(f"{processed_folder_path}/circuits")
# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

 #df = spark.read.parquet(f"{processed_folder_path}/circuits")
 #display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# confirm the data is stored well and read all the files
df = spark.read.format("delta").load(f"{processed_folder_path}/circuits")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### SQL read

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from processed_db.circuits;

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")
