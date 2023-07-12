-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Drop the processed_db and presentation_db

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### load the initial configuration

-- COMMAND ----------

-- MAGIC %run "/formula1/include/configuration"

-- COMMAND ----------

-- MAGIC %run "/formula1/include/common_functions"

-- COMMAND ----------

--all the managed tables and its data in the storage account gets deleted. but in case of the external tables the data in the external table always reside.
DROP DATABASE IF EXISTS processed_db CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS processed_db
LOCATION "/mnt/databrickscourcedl/processed/";

-- COMMAND ----------

--all the managed tables and its data in the storage account gets deleted. but in case of the external tables the data in the external table always reside.
DROP DATABASE IF EXISTS presentation_db CASCADE;

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS presentation_db
LOCATION "/mnt/databrickscourcedl/presentation/";