# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest Constructor.json

# COMMAND ----------

# Include the common files to export the common variable and functions.
# The filename without extention is fine
# "/formula1/include/configuration"
# "/formula1/include/common_functions"

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
dbutils.widgets.text("p_data_source","")
v_data_source = dbutils.widgets.get("p_data_source")
display(v_data_source)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1 : Read the JSON file

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# Prepare the schema either with STRUCT or new method written below
# the below method use the Hive Datetypes.

contructor_schema = "constructorId INT,constructorRef STRING,name STRING,nationality STRING,url STRING"

# COMMAND ----------

contructor_df = spark.read \
.schema(contructor_schema) \
.json(f"{raw_folder_path}/constructors.json")

# COMMAND ----------

display(contructor_df)

# COMMAND ----------

contructor_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 : 3 Way to Removed Unwanted column

# COMMAND ----------

# In the CSV file chapeter we did selection of the limited columns so that other unwanted columns gets dropped out.
# Now we are going to use the new method for the dropping of the columns
# Three ways
# Way 1 : Simple And easy way
contructor_dropped_df = contructor_df.drop("url")

# COMMAND ----------

display(contructor_dropped_df)

# COMMAND ----------

# way 2 
contructor_dropped_df = contructor_df.drop(contructor_df["url"])

# COMMAND ----------

# way 3
from pyspark.sql.functions import col
contructor_dropped_df = contructor_df.drop(col("url"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 : Rename of the columns and add new extra columns

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , lit
constructor_final_df = contructor_dropped_df.withColumnRenamed("constructorId","constructor_id") \
                                            .withColumnRenamed("constructorRef","constructor_ref") \
                                            .withColumn("data_source",lit(v_data_source))

# COMMAND ----------

constructor_final_df = add_ingestion_date(constructor_final_df)

# COMMAND ----------

display(constructor_final_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4 : Write the data in the form of the parquet files

# COMMAND ----------

constructor_final_df.write.mode("overwrite").parquet(f"{processed_folder_path}/constructor")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/databrickscourcedl/processed/constructor

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.parquet(f"{processed_folder_path}/constructor/")

# COMMAND ----------

display(df)

# COMMAND ----------

# this success indicator is required to get the confirmation message for the calling program 0.ingest_all_files
dbutils.notebook.exit("success")