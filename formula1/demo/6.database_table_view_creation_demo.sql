-- Databricks notebook source
-- MAGIC %md
-- MAGIC # In python we prepared the sql dataframe but now we will make the table and views in the Database
-- MAGIC # Run the SQL commands in the SQL editor

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###### load the initial configuration

-- COMMAND ----------

-- MAGIC %run "../include/configuration"

-- COMMAND ----------

-- MAGIC %run "../include/common_functions"

-- COMMAND ----------

-- Create the new database but its not re-runnable
-- as its SQL cells , the python # comment will not work here.
--CREATE DATABASE demo;

-- COMMAND ----------

-- create the re-runnable code
CREATE DATABASE IF NOT EXISTS demo;

-- COMMAND ----------

-- listing all the database without going to Data -> 
SHOW databases;

-- COMMAND ----------

-- the DESC or DESCRIBE both will work.
DESC DATABASE demo;

-- COMMAND ----------

-- the DESC or DESCRIBE both will work. The new Properties column value will comes up.
DESC DATABASE EXTENDED demo;

-- COMMAND ----------

-- by default the notebook database gets loaded with "default" database
-- So any new table will created inside the default database
SELECT CURRENT_DATABASE()

-- COMMAND ----------

-- show the list of the tables in the current database
SHOW TABLES;

-- COMMAND ----------

-- show the list of the tables in the demo database
SHOW TABLES IN demo;

-- COMMAND ----------

--Switch the database from the default to demo
USE demo;

-- COMMAND ----------

SELECT CURRENT_DATABASE()

-- COMMAND ----------

SHOW TABLES;

-- COMMAND ----------

SHOW TABLES IN default;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### ************************************revision old concept************************************

-- COMMAND ----------


----------------------------------------------------READ--------------------------------------------------
--1) READ Python Code
--read the data in the python datafrom from the Data files
--python_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results/")
--python_df = spark.read.csv(f"{raw_folder_path}/races.csv/")
--python_df = spark.read.json(f"{raw_folder_path}/drivers.json/")
--
--2) READ SQL from SQL
--read the data in the SQL cells from the sql views or tables
--select * from v_dashboard_results
--select * from global_temp.gv_dashboard_results
--
--3) READ SQL from Python
--read the data in the python cells from sql views or tables
--python_df = spark.sql("select * from v_dashboard_results")
--python_df = spark.sql("select * from global_temp.gv_dashboard_results")
--
----------------------------------------------------WRITE--------------------------------------------------
--4) WRITE Python to Python Code:
--write the python dataframe data in the storage location
--python_df.write.mode("overwrite").parquet(f"{presentation_folder_path}/dashboard_results")
--
--5) Write Python to SQL Managed Table
--write the python dataframe data in the SQL Managed tables
--python_df.write.format("parquet").saveAsTable("demo.dashboard_results")
--
--6) Write SQL to SQL UnManaged Table
--write the SQL table data in the another SQL Managed tables
--CREATE TABLE demo.dashboard_results_filtered AS SELECT * FROM demo.dashboard_results WHERE race_year = 2020;
--
--7) Write Python to SQL UN-Managed Table
--write the python dataframe data in the SQL UNMANAGED EXTERNAL tables but databricks storage path location
--python_df.write.format("parquet").option("path",f"{presentation_folder_path}/dashboard_results/").saveAsTable("demo.dashboard_results")
--
--8) Write SQL to SQL UN-Managed Table
--write the python dataframe data in the SQL UNMANAGED EXTERNAL tables but ADLS storage path location
--CREATE EXTERNAL Table USING CSV|parquet|JSON LOCATION/OPTION
--INSERT INTO NEW_TABLE SELECT * FROM OLD_TABLE
--
----------------------------------------------------VIEW--------------------------------------------------
--9) Create SQL view by Python
--python_df.createOrReplaceTempView("v_dashboard_results")   
--python_df.createOrReplaceGlobalTempView("gv_dashboard_results")  
--No option for the permenant view creation
--
--10) Create SQL view by SQL
--CREATE OR REPLACE TEMP VIEW v_dashboard_results AS SELECT * FROM TABLE_NAME WHERE ..
--CREATE OR REPLACE GLOBAL TEMP VIEW v_dashboard_results AS SELECT * FROM TABLE_NAME WHERE ..
--CREATE OR REPLACE VIEW v_dashboard_results AS SELECT * FROM TABLE_NAME WHERE .. 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## ----------Managed Table Total 2 Options----------

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## TABLE : Create the Managed table using the Python

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dashboard_result_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results/")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### to make the code re-runnable the mode("overwrite") is required

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dashboard_result_df.write.mode("overwrite").format("parquet").saveAsTable("demo.dashboard_results")

-- COMMAND ----------

SELECT current_database()

-- COMMAND ----------

SHOW TABLES;

-- COMMAND ----------

DESC demo.dashboard_results;

-- COMMAND ----------

DESC EXTENDED demo.dashboard_results;

-- COMMAND ----------

SELECT * FROM demo.dashboard_results WHERE race_year = '2020';

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## TABLE : Create the Managed table using the SQL

-- COMMAND ----------

CREATE TABLE demo.dashboard_results_filtered
AS 
SELECT * FROM demo.dashboard_results
WHERE race_year = 2020;

-- COMMAND ----------

SHOW TABLES;

-- COMMAND ----------

DESC EXTENDED demo.dashboard_results_filtered;

-- COMMAND ----------

-- drop the both table metadata and data
-- the databricks stored the table data also in the form of the parquet format
DROP TABLE demo.dashboard_results_filtered;

-- COMMAND ----------

SHOW TABLES;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## ----------UnManaged Table 2 Options----------

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## TABLE : Create the UNMANGED (external) table using the Python

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### extra syntax .option("path",f"{presentation_folder_path}/dashboard_results_external_table/")
-- MAGIC #### data is stored in the form of the files but this files are save in the azure data lake gen2 storage account

-- COMMAND ----------

--mode("overwrite") is required to make the code re-runnable

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dashboard_result_df.write.mode("overwrite").format("parquet").option("path",f"{presentation_folder_path}/dashboard_results_external_table/").saveAsTable("demo.dashboard_results_external_table")

-- COMMAND ----------

SELECT * FROM demo.dashboard_results_external_table;

-- COMMAND ----------

DESC EXTENDED demo.dashboard_results_external_table;

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## TABLE : Create the UNMANGED (external) table using the SQL

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### the data is stored in the azure gen 2 storage account and both source and destination are the external tables

-- COMMAND ----------

--create the empty table
CREATE TABLE demo.dashboard_results_filtered
(
race_year INT,
race_name STRING,
race_date TIMESTAMP,
circuit_location STRING,
driver_name STRING,
driver_number INT,
driver_nationality STRING,
team STRING,
grid INT,
fastest_lap INT,
race_time STRING,
points FLOAT,
position INT,
created_date TIMESTAMP
)
USING parquet
--LOCATION "{presentation_folder_path}/dashboard_results_filtered"              not working python vaiable in the sql
LOCATION "/mnt/datasourceformula1/presentation/dashboard_results_filtered";

-- COMMAND ----------

--load the data in the empty table
INSERT INTO demo.dashboard_results_filtered
(
race_year,
race_name,
race_date,
circuit_location,
driver_name,
driver_number,
driver_nationality,
team,
grid,
fastest_lap,
race_time,
points,
position,
created_date
)
SELECT 
race_year,
race_name,
race_date,
circuit_location,
driver_name,
driver_number,
driver_nationality,
team,
grid,
fastest_lap,
race_time,
points,
position,
created_date
FROM demo.dashboard_results_external_table WHERE race_year = 2020;

-- COMMAND ----------

SELECT * FROM demo.dashboard_results_filtered;

-- COMMAND ----------

SHOW TABLES IN demo;

-- COMMAND ----------

-- this just dropped the table structure only but the data is still present in the Azure Gen2 storage account
-- So in the case of the external table , the spark manages the meta data only, the data need to managed by users 
DROP TABLE demo.dashboard_results_filtered;

-- COMMAND ----------

SHOW TABLES IN demo;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # VIEW : Create the TEMP View Using the Python

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dashboard_result_df.createOrReplaceTempView("v_dashboard_results")

-- COMMAND ----------

--The local temp view does not have any schema or database , it will NOT available cross notebook and will remain till notebooks session is active
select * from v_dashboard_results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # VIEW : Create the GLOBAL TEMP View Using the Python

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dashboard_result_df.createOrReplaceGlobalTempView("gv_dashboard_results")

-- COMMAND ----------

----The global temp view gets prepared under the DB Or Schema "global_temp" , it will available cross notebook and will remain till cluster is active
select * from global_temp.gv_dashboard_results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # VIEW : Create the TEMP View Using the SQL

-- COMMAND ----------

CREATE OR REPLACE TEMP VIEW v_dashboard_results
AS 
SELECT * FROM demo.dashboard_results
where race_year = 2020

-- COMMAND ----------

--The local temp view does not have any schema or database , it will NOT available cross notebook and will remain till notebooks session is active
select * from v_dashboard_results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # VIEW : Create the GLOBAL TEMP View Using the SQL

-- COMMAND ----------

CREATE OR REPLACE GLOBAL TEMP VIEW gv_dashboard_results
AS 
SELECT * FROM demo.dashboard_results
where race_year = 2020

-- COMMAND ----------

--The global temp view gets prepared under the DB Or Schema "global_temp" , it will available cross notebook and will remain till cluster is active
select * from global_temp.gv_dashboard_results;

-- COMMAND ----------

SHOW TABLES IN global_temp;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Permenant View using the SQL

-- COMMAND ----------

CREATE OR REPLACE VIEW demo.pv_dashboard_results
AS 
SELECT * FROM demo.dashboard_results
where race_year = 2020;

-- COMMAND ----------

select * from demo.pv_dashboard_results;

-- COMMAND ----------

SHOW TABLES IN demo;
