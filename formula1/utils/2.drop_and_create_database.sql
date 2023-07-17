-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Drop the processed_db and presentation_db

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### load the initial configuration

-- COMMAND ----------

-- MAGIC %run "../include/configuration"

-- COMMAND ----------

-- MAGIC %run "../include/common_functions"

-- COMMAND ----------

-- MAGIC %python
-- MAGIC # check the list of the all the mounts before run
-- MAGIC dbutils.fs.mounts()

-- COMMAND ----------

--all the managed tables and its data in the storage account gets deleted. but in case of the external tables the data in the external table always reside.
DROP DATABASE IF EXISTS raw_db CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS raw_db;

-- COMMAND ----------

--all the managed tables and its data in the storage account gets deleted. but in case of the external tables the data in the external table always reside.
DROP DATABASE IF EXISTS processed_db CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS processed_db
LOCATION "/mnt/datasourceformula1/processed/";

-- COMMAND ----------

--all the managed tables and its data in the storage account gets deleted. but in case of the external tables the data in the external table always reside.
DROP DATABASE IF EXISTS presentation_db CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS presentation_db
LOCATION "/mnt/datasourceformula1/presentation/";

-- COMMAND ----------

-- MAGIC %python
-- MAGIC # check the list of the all the mounts before run
-- MAGIC dbutils.fs.mounts()
