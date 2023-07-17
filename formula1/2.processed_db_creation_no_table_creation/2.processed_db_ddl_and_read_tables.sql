-- Databricks notebook source
-- MAGIC %md
-- MAGIC # NOTE:
-- MAGIC ### The processed DB is made in the advanced and the tables for the processed db can be made external like its made in the raw_db external tables.
-- MAGIC ### But the good design approch is make the permenant tables 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # The Processed files are saved under the Azure data factory, now same files will be access in the SQL using the Tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Load the configuration files

-- COMMAND ----------

-- MAGIC %run "../include/configuration"

-- COMMAND ----------

-- MAGIC %run "../include/common_functions"

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### database made inside  of the ADLS location
-- MAGIC
-- MAGIC ##### dbfs:/mnt/datasourceformula1/processed

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS processed_db
LOCATION "/mnt/datasourceformula1/processed";

-- COMMAND ----------

--we can make the database under the provide databricks mount point location which is pointing to the Azure Gen2 storage account
--dbfs:/mnt/datasourceformula1/processed
DESC DATABASE processed_db;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # DATA Lake : Read all the processed dataframe 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits")
-- MAGIC #races_df = spark.read.parquet(f"{processed_folder_path}/races")
-- MAGIC #constructor_df = spark.read.parquet(f"{processed_folder_path}/constructor")
-- MAGIC #drivers_df = spark.read.parquet(f"{processed_folder_path}/drivers")
-- MAGIC #results_df = spark.read.parquet(f"{processed_folder_path}/results")
-- MAGIC #pit_stop_df = spark.read.parquet(f"{processed_folder_path}/pit_stops")
-- MAGIC #lap_times_df = spark.read.parquet(f"{processed_folder_path}/lap_times")
-- MAGIC #qualifying_df = spark.read.parquet(f"{processed_folder_path}/qualifying")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # DELTA Lake : Read all the processed dataframe 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #circuits_df = spark.read.format("delta").load(f"{processed_folder_path}/circuits")
-- MAGIC #races_df = spark.read.format("delta").load(f"{processed_folder_path}/races")
-- MAGIC #constructor_df = spark.read.format("delta").load(f"{processed_folder_path}/constructor")
-- MAGIC #drivers_df = spark.read.format("delta").load(f"{processed_folder_path}/drivers")
-- MAGIC #results_df = spark.read.format("delta").load(f"{processed_folder_path}/results")
-- MAGIC #pit_stop_df = spark.read.format("delta").load(f"{processed_folder_path}/pit_stops")
-- MAGIC #lap_times_df = spark.read.format("delta").load(f"{processed_folder_path}/lap_times")
-- MAGIC #qualifying_df = spark.read.format("delta").load(f"{processed_folder_path}/qualifying")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # SQL : Read all the processed data from database 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1) PROCESSED TABLE processed_db.circuits from Parquet file

-- COMMAND ----------

select * from processed_db.circuits;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2) PROCESSED TABLE processed_db.races from Parquet file

-- COMMAND ----------

select * from processed_db.races;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3) PROCESSED TABLE processed_db.constructors from Parquet file

-- COMMAND ----------

select * from processed_db.constructor;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 4) PROCESSED TABLE processed_db.drivers from Parquet file

-- COMMAND ----------

select * from processed_db.drivers;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 5) PROCESSED TABLE processed_db.results from Parquet file

-- COMMAND ----------

select * from processed_db.results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 6) PROCESSED TABLE processed_db.pit_stops from Parquet file

-- COMMAND ----------

select * from processed_db.pit_stops;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 7) PROCESSED TABLE processed_db.lap_times from Parquet file

-- COMMAND ----------

select * from processed_db.lap_times;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 8) PROCESSED TABLE processed_db.qualifying from Parquet file

-- COMMAND ----------

select * from processed_db.qualifying;
