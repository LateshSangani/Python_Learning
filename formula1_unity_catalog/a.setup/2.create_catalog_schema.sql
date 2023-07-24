-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### Create the Catalog and Schema required for the project Formula1 with UC 
-- MAGIC #### 1) Catalog : formula1_dev(Without Managed Location)
-- MAGIC #### 2) Schemas : bronze,silver,gold(With Managed Location)
-- MAGIC

-- COMMAND ----------

--From UI the catalog made with below approch.
--Open the databricks workspace URL -> Data Explorer -> Create Catalog -> demo_catalog

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###### SQL way to make the external location

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS formula1_dev

-- COMMAND ----------

USE CATALOG formula1_dev

-- COMMAND ----------

--From UI the Schrma made with below approch.
--Open the databricks workspace URL -> Data Explorer -> Catalog List -> demo_catalog -> Create Schema -> demo_schema

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS bronze
MANAGED LOCATION "abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/"

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS silver
MANAGED LOCATION "abfss://silver@datasourceformula1ucext.dfs.core.windows.net/"

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS gold
MANAGED LOCATION "abfss://gold@datasourceformula1ucext.dfs.core.windows.net/"

-- COMMAND ----------

SHOW SCHEMAS
