# Databricks notebook source
# MAGIC %md
# MAGIC ### Multiple way to read the columns from the dataframes

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

circuits_df = spark.read \
.option("header" ,True) \
.option("inferSchema", True) \
.csv("/mnt/datasourceformula1/raw/circuits.csv")
display(circuits_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Multiple way to select the full or filter data

# COMMAND ----------

circuits_final_df = circuits_df.select("*")
circuits_final_df.display()

# COMMAND ----------

circuits_final_df = circuits_df.select("circuitId","name","location")
circuits_final_df.display()

# COMMAND ----------

circuits_final_df = circuits_df.select(circuits_df.circuitId,circuits_df.name,circuits_df.location)
circuits_final_df.display()

# COMMAND ----------

circuits_final_df = circuits_df.select(circuits_df["circuitId"],circuits_df["name"],circuits_df["location"])
circuits_final_df.display()

# COMMAND ----------

from pyspark.sql.functions import col
circuits_final_df = circuits_df.select(col("circuitId"),col("name"),col("location").alias("Circuid_Location"))
circuits_final_df.display()

# COMMAND ----------

circuits_final_df.write.parquet("/mnt/datasourceformula1/processed/circuits")

# COMMAND ----------

circuits_final_df.write.mode("overwrite").parquet("/mnt/datasourceformula1/processed/circuits")

# COMMAND ----------

df = spark.read.parquet("/mnt/datasourceformula1/processed/circuits")

# COMMAND ----------

df.display()
