# Databricks notebook source
# MAGIC %md 
# MAGIC ## Load All Initial configuration files

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All the Widgets

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is 2099-01-01  , but it can be anything we defined.
dbutils.widgets.text("p_as_of_date","2099-01-01")
v_as_of_date = dbutils.widgets.get("p_as_of_date")
display(v_as_of_date)

# COMMAND ----------

# calculated_points logic : If the driver comes on the 10th position, he will get 0 point, if the driver comes on the 1st position he will get the 9 points
# Create the table to save the output of the SELECT query for the future analysis
# As this select query output is required for the presentation purpose , the table is requried to make under the presentation_db
spark.sql(
f"""CREATE TABLE IF NOT EXISTS presentation_db.calculated_race_results
(
race_year INT,
constructor_name STRING,
driver_id INT,
driver_name STRING,
race_id INT,
position INT,
actual_points INT,
calculated_points INT,
created_date TIMESTAMP,
updated_date TIMESTAMP
)
USING DELTA
""")

# COMMAND ----------

# Benifit with spark.sql is that we can now python variable as input parameter and make the notebook full of the python only.
spark.sql(f"""
CREATE OR REPLACE TEMP VIEW v_calculated_race_results_temp
AS
SELECT a.race_year, c.name as constructor_name , d.driver_id , d.name driver_name , r.race_id , r.position , r.points as actual_points,
11 - r.position as calculated_points
FROM processed_db.results r 
JOIN processed_db.drivers d ON (r.driver_id = d.driver_id)
JOIN processed_db.constructor c ON (r.constructor_id = c.constructor_id)
JOIN processed_db.races a ON (r.race_id = a.race_id)
WHERE r.position <= 10
AND r.as_of_date = '{v_as_of_date}'
""")


# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from v_calculated_race_results_temp

# COMMAND ----------

spark.sql(f"""
MERGE INTO presentation_db.calculated_race_results target
USING v_calculated_race_results_temp upd
ON (target.driver_id = upd.driver_id AND target.race_id = upd.race_id)
WHEN MATCHED THEN 
UPDATE SET target.position = upd.position,
target.actual_points = upd.actual_points,
target.calculated_points = upd.calculated_points,
target.updated_date = current_timestamp
WHEN NOT MATCHED
THEN INSERT (race_year,constructor_name,driver_id,driver_name,race_id,position,actual_points,calculated_points,created_date) 
VALUES (race_year,constructor_name,driver_id,driver_name,race_id,position,actual_points,calculated_points,current_timestamp)
""")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from presentation_db.calculated_race_results

# COMMAND ----------


