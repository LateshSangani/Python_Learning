# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest Drivers.json

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
# MAGIC ## Step 1 : Read the JSON file

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------



# COMMAND ----------

from pyspark.sql.types import StructType,StructField, IntegerType , StringType , DateType

# COMMAND ----------

name_schema = StructType(fields = [StructField("forename",StringType(),True), \
                                  StructField("surname",StringType(),True) \
                                 
])

# COMMAND ----------

drivers_schema = StructType(fields = [StructField("driverId",IntegerType(),False),
                                      StructField("driverRef",StringType(),True),
                                      StructField("number",IntegerType(),True),
                                      StructField("code",StringType(),True),
                                      StructField("name",name_schema,True),   # name_schema prepared in the above step.
                                      StructField("dob",DateType(),True),
                                      StructField("nationality",StringType(),True),
                                      StructField("url",StringType(),True)                                 
])

# COMMAND ----------

drivers_df = spark.read \
.schema(drivers_schema) \
.json(f"{raw_folder_path}/{v_as_of_date}/drivers.json")

# COMMAND ----------

display(drivers_df)

# COMMAND ----------

#drivers_df.schema.names
drivers_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : Rename of the columns , add new extra columns , removed unwanted column

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit
drivers_final_df = drivers_df.withColumnRenamed("driverId","driver_id") \
                            .withColumnRenamed("driverRef","driver_ref") \
                            .withColumn("name",concat(col("name.forename"), lit(" ") , col("name.surname"))) \
                            .withColumn("data_source",lit(v_data_source)) \
                            .withColumn("as_of_date",lit(v_as_of_date)) \
                            .drop(col("url"))

# COMMAND ----------

drivers_final_df = add_ingestion_date(drivers_final_df)

# COMMAND ----------

display(drivers_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Write the data in the form of the parquet files

# COMMAND ----------

# drivers_final_df.write.mode("overwrite").parquet(f"{processed_folder_path}/drivers")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### full load with data lake

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# drivers_final_df.write.mode("overwrite").format("parquet").saveAsTable("processed_db.drivers")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### full load with delta lake

# COMMAND ----------

drivers_final_df.write.mode("overwrite").format("delta").saveAsTable("processed_db.drivers")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

# df = spark.read.parquet(f"{processed_folder_path}/drivers")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.format("delta").load(f"{processed_folder_path}/drivers")

# COMMAND ----------

display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")