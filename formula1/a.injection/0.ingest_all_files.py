# Databricks notebook source
# MAGIC %md
# MAGIC #### This is the main calling file which will call internally all the 8 data source child files 1 by 1.
# MAGIC #### The parallel execution also possible but spark has some limitations on it.
# MAGIC #### This file can run the manually OR the job formula1_ingestion_job is prepared to run the file.
# MAGIC #### The job formula1_ingestion_job used the new Cluster "formula1_ingestion_cluster" , this cluster get preapared automatacally after the job run and every time after jobs execution is done, it will be dicommision.
# MAGIC #### the next job run will make again new job cluster

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All Initial configuration files

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Load All the Widgets

# COMMAND ----------

#The manual run of the many of the notebooks can be run all together to have data with single run.
# 1st parameter is notebook full path , second is timeout seconds , third is dictionry array
# the v_result will get the values from the source file. as the last of the source file the dbutils.notebook.exit("success") is written.

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
dbutils.widgets.text("p_data_source","")
v_data_source = dbutils.widgets.get("p_data_source")
display(v_data_source)

# COMMAND ----------

# add the input parameter of widget
# the input parameter can be used to filter the data or store the extra column
# the default value is 2099-01-01  , but it can be anything we defined.
dbutils.widgets.text("p_as_of_date","2099-01-01")
v_as_of_date = dbutils.widgets.get("p_as_of_date")
display(v_as_of_date)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Run all the notebooks

# COMMAND ----------

v_result = dbutils.notebook.run("1.ingest_circuits_file_csv",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("2.ingest_races_file_csv",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("3.ingest_contructor_file_json",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("4.ingest_drivers_file_json_array",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("5.ingest_results_file_json",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("6.ingest_pitstop_file_multiline_json",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("7.ingest_lap_times_file_multi_csv",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

v_result = dbutils.notebook.run("8.ingest_qualifying_file_multiline_multiple_json",0,{"p_data_source" : v_data_source  , "p_as_of_date" : v_as_of_date} )
v_result

# COMMAND ----------

# MAGIC %md 
# MAGIC # confirm the results for all the tables

# COMMAND ----------

# MAGIC %sql
# MAGIC REFRESH TABLE processed_db.circuits;
# MAGIC REFRESH TABLE processed_db.races;
# MAGIC REFRESH TABLE processed_db.constructor;
# MAGIC REFRESH TABLE processed_db.drivers;
# MAGIC REFRESH TABLE processed_db.results;
# MAGIC REFRESH TABLE processed_db.pit_stops;
# MAGIC REFRESH TABLE processed_db.lap_times;
# MAGIC REFRESH TABLE processed_db.qualifying;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.circuits group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.races group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.constructor group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.drivers group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.results group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.pit_stops group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.lap_times group by as_of_date;

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from processed_db.qualifying group by as_of_date;
