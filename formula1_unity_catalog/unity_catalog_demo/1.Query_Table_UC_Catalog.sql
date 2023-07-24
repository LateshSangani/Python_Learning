-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Query table using the three level name space

-- COMMAND ----------

select * from demo_catalog.demo_schema.circuits

-- COMMAND ----------

select current_catalog()

-- COMMAND ----------

SHOW CATALOGS

-- COMMAND ----------

USE CATALOG demo_catalog

-- COMMAND ----------

select * from demo_schema.circuits;

-- COMMAND ----------

select current_schema()

-- COMMAND ----------

SHOW SCHEMAS

-- COMMAND ----------

USE SCHEMA demo_schema

-- COMMAND ----------

select * from circuits

-- COMMAND ----------

SHOW tables

-- COMMAND ----------

-- MAGIC %python
-- MAGIC spark.sql("select * from demo_catalog.demo_schema.circuits").display()

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df = spark.table("demo_catalog.demo_schema.circuits")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df.display()
