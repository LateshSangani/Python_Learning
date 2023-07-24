-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Create the Gold tables using Managed tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### formula1_dev.gold.driver_wins Table from formula1_dev.silver.drivers and formula1_dev.silver.results

-- COMMAND ----------

DROP TABLE IF EXISTS formula1_dev.gold.driver_wins;
CREATE TABLE IF NOT EXISTS formula1_dev.gold.driver_wins
AS
SELECT
  d.name,
  count(1) as number_of_wins
FROM formula1_dev.silver.drivers d JOIN formula1_dev.silver.results r
ON (d.driver_id = r.driver_id)
WHERE r.position = 1
GROUP BY d.name

-- COMMAND ----------

SELECT
  d.name,
  count(1) as number_of_wins
FROM formula1_dev.silver.drivers d JOIN formula1_dev.silver.results r
ON (d.driver_id = r.driver_id)
WHERE r.position = 1
GROUP BY d.name
ORDER BY d.name

-- COMMAND ----------

select * from formula1_dev.gold.driver_wins order by name;
