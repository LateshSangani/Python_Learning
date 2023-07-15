# Databricks notebook source
# MAGIC %md
# MAGIC ## The global view made on the 5.sql_global_view_demo.py is accesable from the current notebook

# COMMAND ----------

# MAGIC %sql
# MAGIC select race_year,count(*),max(fastest_lap),min(fastest_lap),sum(points),avg(race_time)
# MAGIC from global_temp.gv_dashboard_results
# MAGIC group by race_year
# MAGIC order by race_year desc
