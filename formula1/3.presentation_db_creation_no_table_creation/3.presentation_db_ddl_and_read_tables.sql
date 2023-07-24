-- Databricks notebook source
-- MAGIC %md
-- MAGIC # NOTE:
-- MAGIC ### The presentation DB is made in the advanced and the tables for the presentation db can be made external like its made in the raw_db external tables.
-- MAGIC ### But the good design approch is make the permenant tables like we did in the processed table

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # The presentation files are saved under the Azure data factory, now same files will be access in the SQL using the Tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Load the configuration files

-- COMMAND ----------

-- MAGIC %run "../include/configuration"

-- COMMAND ----------

-- MAGIC %run "../include/common_functions"

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS presentation_db
LOCATION "/mnt/datasourceformula1/presentation";

-- COMMAND ----------

--we can make the database under the provide databricks mount point location which is pointing to the Azure Gen2 storage account
--dbfs:/mnt/databrickscourcedl/presentation
DESC DATABASE presentation_db

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # DATA Lake: Read all presentation dataframe

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #dashboard_results_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")
-- MAGIC #dashboard_standings_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_standings")
-- MAGIC #dashboard_constructor_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_constructor")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # DELTA Lake: Read all presentation dataframe

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #dashboard_results_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results")
-- MAGIC #dashboard_standings_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_standings")
-- MAGIC #dashboard_constructor_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_constructor")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1) PRESENTATION TABLE presentation_db.dashboard_results from Parquet file

-- COMMAND ----------

select * from presentation_db.dashboard_results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2) PRESENTATION TABLE presentation_db.dashboard_contructor from Parquet file

-- COMMAND ----------

select * from presentation_db.dashboard_constructor;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3) PRESENTATION TABLE presentation_db.dashboard_standings from Parquet file

-- COMMAND ----------

select * from presentation_db.dashboard_standings;
