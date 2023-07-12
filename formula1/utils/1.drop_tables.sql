-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Drop the processed_db and presentation_db tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### load the initial configuration

-- COMMAND ----------

-- MAGIC %run "/formula1/include/configuration"

-- COMMAND ----------

-- MAGIC %run "/formula1/include/common_functions"

-- COMMAND ----------

drop table processed_db.circuits;

-- COMMAND ----------

drop table processed_db.races;

-- COMMAND ----------

drop table processed_db.constructor;

-- COMMAND ----------

drop table processed_db.drivers;

-- COMMAND ----------

drop table processed_db.results;

-- COMMAND ----------

drop table processed_db.pit_stops;

-- COMMAND ----------

drop table processed_db.lap_times;

-- COMMAND ----------

drop table processed_db.qualifying;

-- COMMAND ----------

drop table presentation_db.dashboard_results;

-- COMMAND ----------

drop table presentation_db.dashboard_standings;

-- COMMAND ----------

drop table presentation_db.dashboard_constructor;

-- COMMAND ----------

drop table presentation_db.calculated_race_results;