-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Create the Silver tables using Managed tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### formula1_dev.silver.drivers Table from formula1_dev.bronze.drivers

-- COMMAND ----------

DROP TABLE IF EXISTS formula1_dev.silver.drivers;
CREATE TABLE IF NOT EXISTS formula1_dev.silver.drivers
AS
SELECT
  driverId AS driver_id,
  driverRef AS driver_ref,
  number,
  code,
  concat(name.forename,' ',name.surname) as name,
  dob,
  nationality,
  current_timestamp() as ingestion_date
FROM formula1_dev.bronze.drivers;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### formula1_dev.silver.results Table from formula1_dev.bronze.results

-- COMMAND ----------

DROP TABLE IF EXISTS formula1_dev.silver.results;
CREATE TABLE IF NOT EXISTS formula1_dev.silver.results
AS
SELECT
resultId AS result_id,
raceId as race_id,
driverId as driver_id,
constructorId as contructor_id,
number,
grid,
position,
positionText,
positionOrder,
points,
laps,
time,
milliseconds,
fastestLap,
rank,
fastestLapTime,
fastestLapSpeed,
statusId,
current_timestamp() as ingestion_date
FROM formula1_dev.bronze.results;


-- COMMAND ----------

select * from formula1_dev.silver.drivers;

-- COMMAND ----------

select * from formula1_dev.silver.results;
