-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Create the Bronze tables using external tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### formula1_dev.bronze.drivers Table from drivers.json

-- COMMAND ----------

DROP TABLE IF EXISTS formula1_dev.bronze.drivers;
CREATE TABLE IF NOT EXISTS formula1_dev.bronze.drivers
(
driverId INT,
driverRef STRING,
number INT,
code STRING,
name STRUCT<forename:string,surname string>,
dob DATE,
nationality STRING,
url STRING
)
USING JSON
OPTIONS(path "abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/drivers.json");

-- COMMAND ----------

DROP TABLE IF EXISTS formula1_dev.bronze.results;
CREATE TABLE IF NOT EXISTS formula1_dev.bronze.results
(
resultId INT,
raceId INT,
driverId INT,
constructorId INT,
number INT,
grid INT,
position INT,
positionText STRING,
positionOrder INT,
points FLOAT,
laps INT,
time STRING,
milliseconds INT,
fastestLap INT,
rank INT,
fastestLapTime STRING,
fastestLapSpeed STRING,
statusId INT
)
USING JSON
OPTIONS(path "abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/results.json");

-- COMMAND ----------

select * from formula1_dev.bronze.drivers;

-- COMMAND ----------

select * from formula1_dev.bronze.results;
