# Databricks notebook source
# MAGIC %md
# MAGIC # SQL Access of the Python Dataframe

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Load the initial configuration

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create the Global temporary view on the Dataframe

# COMMAND ----------

# MAGIC %md
# MAGIC ##### the global temporary view is available out side of session , so when cluster gets de-attached or attached this view will still exists.
# MAGIC ##### the global temporary view will be not available ,after cluster get terminated.
# MAGIC ##### the global temporary view can be shared with other notebooks with in the session.
# MAGIC ##### just plain createGlobalTempView also worked but its not re-runnable. the createOrReplaceGlobalTempView will make the re-runnable code

# COMMAND ----------

sql_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

sql_df.createOrReplaceGlobalTempView("gv_dashboard_results")  # gv : global_view

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN global_temp;

# COMMAND ----------

# MAGIC %md
# MAGIC # Approch 1 : Reading SQL from the SQL cells

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 1) the sql cell does not return any dataframe which can be stored some where.
# MAGIC ##### 2) the sql cell running in the Python notbooks does not accept any input parameter or paramter coming from the widget
# MAGIC ##### 3) in standard programming its used to just analysied the data.
# MAGIC ##### 4) the global view stored in the default database global_temp

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.gv_dashboard_results where race_year = 2020

# COMMAND ----------

# MAGIC %md
# MAGIC #####  Aggregration Function Testing

# COMMAND ----------

# MAGIC %sql
# MAGIC select race_year,count(*),max(fastest_lap),min(fastest_lap),sum(points),avg(race_time)
# MAGIC from global_temp.gv_dashboard_results
# MAGIC group by race_year
# MAGIC order by race_year desc

# COMMAND ----------

# MAGIC %md
# MAGIC # Approch 2 : Reading SQL from the Python Cell

# COMMAND ----------

sql_df = spark.sql("select * from global_temp.gv_dashboard_results")

# COMMAND ----------

sql_df = spark.sql(f"select * from global_temp.gv_dashboard_results where race_year = 2020")
sql_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### python with input parameter of the race_year

# COMMAND ----------

p_race_year = 2020
sql_df = spark.sql(f"select * from global_temp.gv_dashboard_results where race_year = {p_race_year}")
sql_df.display()
