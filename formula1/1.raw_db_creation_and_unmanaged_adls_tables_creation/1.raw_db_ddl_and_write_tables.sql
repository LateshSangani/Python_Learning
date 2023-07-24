-- Databricks notebook source
-- MAGIC %md
-- MAGIC # The raw files are saved under the Azure data factory, now same files will be access in the SQL using the EXTERNAL Tables

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## Load All Initial configuration files

-- COMMAND ----------

-- MAGIC %run "../include/configuration"

-- COMMAND ----------

-- MAGIC %run "../include/common_functions"

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## Load All the Widgets

-- COMMAND ----------

-- MAGIC %python
-- MAGIC #add the input parameter of widget
-- MAGIC #the input parameter can be used to filter the data or store the extra column
-- MAGIC #the default value is 2099-01-01  , but it can be anything we defined.
-- MAGIC dbutils.widgets.text("p_as_of_date","2099-01-01")
-- MAGIC v_as_of_date = dbutils.widgets.get("p_as_of_date")
-- MAGIC display(v_as_of_date)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Prapare the new Fresh database to stored the Raw Information

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### database made inside  of the default databricks location
-- MAGIC
-- MAGIC ##### dbfs:/user/hive/warehouse/

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS raw_db;

-- COMMAND ----------

--The database gets prapared under the Databricks location "dbfs:/user/hive/warehouse/raw_db.db"
--we can make the database under the provide databricks mount point location which is pointing to the Azure Gen2 storage account
DESC DATABASE raw_db;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Setup of all the UNMANGED Tables where data will stored in the ADLS storage not in the databricks storage

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### NOTE : In this case this unmanaged option will not valid as it stored the data in the databricks storage fixed path.
-- MAGIC ##### df.write.mode("overwrite").format("csv").option("path",f"{raw_folder_path}/circuites.csv/").saveAsTable("raw_db.circuites")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 1) RAW TABLE raw_db.circuits from plain CSV file

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###### note : The "options" section tell from where to read the file and write in the table
-- MAGIC ######        but the "location" section tell where to write the content 

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.circuits;
CREATE TABLE IF NOT EXISTS raw_db.circuits
(
circuitRef string,
name string,
location string,
country string,
lat double,
lng double,
alt int,
url string
)
USING CSV
OPTIONS(path "/mnt/datasourceformula1/raw/circuits.csv", header true);
--LOCATION "/mnt/datasourceformula1/raw/circuits";

-- COMMAND ----------

select * from raw_db.circuits;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 2) RAW TABLE raw_db.races from plain CSV file

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.races;
CREATE TABLE IF NOT EXISTS raw_db.races
(
raceId int,
year int,
round int,
circuitId int,
name string,
date date,
time string,
url string
)
USING CSV
OPTIONS(path "/mnt/datasourceformula1/raw/races.csv", header true);

-- COMMAND ----------

select * from raw_db.races

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 3) RAW TABLE raw_db.constructors from single line JSON file

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.constructors;
CREATE TABLE IF NOT EXISTS raw_db.constructors
(
constructorId INT,
constructorRef STRING,
name STRING,
nationality STRING,
url STRING
)
USING JSON
OPTIONS(path "/mnt/datasourceformula1/raw/constructors.json");

-- COMMAND ----------

select * from raw_db.constructors;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 4) RAW TABLE raw_db.drivers from single line JSON file but multiple values

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.drivers;
CREATE TABLE IF NOT EXISTS raw_db.drivers
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
OPTIONS(path "/mnt/datasourceformula1/raw/drivers.json");

-- COMMAND ----------

select * from raw_db.drivers;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 5) RAW TABLE raw_db.results from single line JSON file

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.results;
CREATE TABLE IF NOT EXISTS raw_db.results
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
OPTIONS(path "/mnt/datasourceformula1/raw/results.json");

-- COMMAND ----------

select * from  raw_db.results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 6) RAW TABLE raw_db.pit_stops from SINGLE JSON Multiline file

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.pit_stops;
CREATE TABLE IF NOT EXISTS raw_db.pit_stops
(
raceId INT,
driverId INT,
stop STRING,
lag INT,
time STRING,
duration STRING,
milliseconds INT
)
USING JSON
OPTIONS(path "/mnt/datasourceformula1/raw/pit_stops.json" , multiLine true);

-- COMMAND ----------

select * from raw_db.pit_stops;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 7) RAW TABLE raw_db.lap_times from Multiple CSV files in Folder

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.lap_times;
CREATE TABLE IF NOT EXISTS raw_db.lap_times
(
raceId int,
driverId int,
lap int,
lag int,
position int,
time string,
milliseconds int
)
USING CSV
OPTIONS(path "/mnt/datasourceformula1/raw/lap_times/", header true);

-- COMMAND ----------

select * from raw_db.lap_times;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## 8) RAW TABLE raw_db.qualifying from Multiple JSON , Multiline files in Folder

-- COMMAND ----------

DROP TABLE IF EXISTS raw_db.qualifying;
CREATE TABLE IF NOT EXISTS raw_db.qualifying
(
qualifyId INT,
raceId INT,
driverId INT,
constructorId INT,
number INT,
position INT,
q1 STRING,
q2 STRING,
q3 STRING
)
USING JSON
OPTIONS(path "/mnt/datasourceformula1/raw/qualifying/" , multiLine true);

-- COMMAND ----------

select * from raw_db.qualifying;
