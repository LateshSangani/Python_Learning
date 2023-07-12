# Databricks notebook source
# MAGIC %md
# MAGIC # SQL Access of the Python Dataframe

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Load the initial configuration

# COMMAND ----------

# MAGIC %run "/formula1/include/configuration"

# COMMAND ----------

# MAGIC %run "/formula1/include/common_functions"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create the temporary view on the Dataframe

# COMMAND ----------

# MAGIC %md
# MAGIC ##### the temporary view is temporary with session , so when cluster gets de-attached or terminated this view will lost
# MAGIC ##### the temporary view cannot be shared with other notebooks with in the session.
# MAGIC ##### just plain createTempView also worked but its not re-runnable. the createOrReplaceTempView will make the re-runnable code

# COMMAND ----------

sql_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

sql_df.createOrReplaceTempView("v_dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC # Reading SQL from the Python %sql cells

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 1) the sql cell does not return any dataframe which can be stored some where.
# MAGIC ##### 2) the sql cell running in the Python notbooks does not accept any input parameter or paramter coming from the widget
# MAGIC ##### 3) in standard programming its used to just analysied the data.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from v_dashboard_results where race_year = 2020

# COMMAND ----------

# MAGIC %md
# MAGIC #####  Aggregration Function Testing

# COMMAND ----------

# MAGIC %sql
# MAGIC select race_year,count(*),max(fastest_lap),min(fastest_lap),sum(points),avg(race_time)
# MAGIC from v_dashboard_results
# MAGIC group by race_year
# MAGIC order by race_year desc

# COMMAND ----------

# MAGIC %md
# MAGIC # Reading SQL from the Python Cell

# COMMAND ----------

sql_df = spark.sql("select * from v_dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### python with input parameter of the race_year

# COMMAND ----------

p_race_year = 2020
sql_df = spark.sql(f"select * from v_dashboard_results where race_year = {p_race_year}")

# COMMAND ----------

sql_df.display()

# COMMAND ----------

