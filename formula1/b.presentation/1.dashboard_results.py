# Databricks notebook source
# MAGIC %md
# MAGIC # Load the inital configurations files

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

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

# MAGIC %md
# MAGIC #-----------------------------------READ-------------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC # Master Data:
# MAGIC #Read all the FULL LOAD data Sources Master table i.e Less Frequentely Modifed Data

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquet files stored ADLS

# COMMAND ----------

#circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits") \
#.withColumnRenamed("name","circuit_name") \
#.withColumnRenamed("location","circuit_location")
#
#races_df = spark.read.parquet(f"{processed_folder_path}/races") \
#.withColumnRenamed("name","race_name") \
#.withColumnRenamed("race_timestamp","race_date")
#
#constructor_df = spark.read.parquet(f"{processed_folder_path}/constructor") \
#.withColumnRenamed("name","team")
#
#drivers_df = spark.read.parquet(f"{processed_folder_path}/drivers") \
#.withColumnRenamed("name","driver_name") \
#.withColumnRenamed("number","driver_number") \
#.withColumnRenamed("nationality","driver_nationality")

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquest files stored in ADLS made by the Managed Tables from the Injection scripts

# COMMAND ----------

#circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits") \
#.withColumnRenamed("name","circuit_name") \
#.withColumnRenamed("location","circuit_location")
#
#races_df = spark.read.parquet(f"{processed_folder_path}/races") \
#.withColumnRenamed("name","race_name") \
#.withColumnRenamed("race_timestamp","race_date")
#
#constructor_df = spark.read.parquet(f"{processed_folder_path}/constructor") \
#.withColumnRenamed("name","team")
#
#drivers_df = spark.read.parquet(f"{processed_folder_path}/drivers") \
#.withColumnRenamed("name","driver_name") \
#.withColumnRenamed("number","driver_number") \
#.withColumnRenamed("nationality","driver_nationality")

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquest files stored in ADLS made by the Managed "DELTA" Tables from the Injection scripts

# COMMAND ----------

circuits_df = spark.read.format("delta").load(f"{processed_folder_path}/circuits") \
.withColumnRenamed("name","circuit_name") \
.withColumnRenamed("location","circuit_location")
#
races_df = spark.read.format("delta").load(f"{processed_folder_path}/races") \
.withColumnRenamed("name","race_name") \
.withColumnRenamed("race_timestamp","race_date")
#
constructor_df = spark.read.format("delta").load(f"{processed_folder_path}/constructor") \
.withColumnRenamed("name","team")
#
drivers_df = spark.read.format("delta").load(f"{processed_folder_path}/drivers") \
.withColumnRenamed("name","driver_name") \
.withColumnRenamed("number","driver_number") \
.withColumnRenamed("nationality","driver_nationality")

# COMMAND ----------

# MAGIC %md
# MAGIC # Transactional Data :
# MAGIC #Read all the INCREMENTAL LOAD data Sources Transaction table i.e Most Frequentely Modifed Data

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquest files stored ADLS

# COMMAND ----------

#results_df = spark.read.parquet(f"{processed_folder_path}/results") \
#.withColumnRenamed("fastestLap","fastest_lap") \
#.withColumnRenamed("time","race_time") \
#.filter(f" as_of_date = '{v_as_of_date}' ")
#
#pit_stop_df = spark.read.parquet(f"{processed_folder_path}/pit_stops") \
#.filter(f" as_of_date = '{v_as_of_date}' ")
#
#lap_times_df = spark.read.parquet(f"{processed_folder_path}/lap_times") \
#.filter(f" as_of_date = '{v_as_of_date}' ") 
#
#qualifying_df = spark.read.parquet(f"{processed_folder_path}/qualifying") \
#.filter(f" as_of_date = '{v_as_of_date}' ")

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquest files stored in ADLS made by the Managed Tables from the Injection scripts

# COMMAND ----------

#results_df = spark.read.parquet(f"{processed_folder_path}/results") \
#.withColumnRenamed("fastestLap","fastest_lap") \
#.withColumnRenamed("time","race_time") \
#.filter(f" as_of_date = '{v_as_of_date}' ")
#
#pit_stop_df = spark.read.parquet(f"{processed_folder_path}/pit_stops") \
#.filter(f" as_of_date = '{v_as_of_date}' ")
#
#lap_times_df = spark.read.parquet(f"{processed_folder_path}/lap_times") \
#.filter(f" as_of_date = '{v_as_of_date}' ") 
#
#qualifying_df = spark.read.parquet(f"{processed_folder_path}/qualifying") \
#.filter(f" as_of_date = '{v_as_of_date}' ")

# COMMAND ----------

# MAGIC %md
# MAGIC #### READ data using python having parquest files stored in ADLS made by the Managed "DELTA" Tables from the Injection scripts

# COMMAND ----------

results_df = spark.read.format("delta").load(f"{processed_folder_path}/results") \
.withColumnRenamed("fastestLap","fastest_lap") \
.withColumnRenamed("time","race_time") \
.filter(f" as_of_date = '{v_as_of_date}' ")

pit_stop_df = spark.read.format("delta").load(f"{processed_folder_path}/pit_stops") \
.filter(f" as_of_date = '{v_as_of_date}' ")

lap_times_df = spark.read.format("delta").load(f"{processed_folder_path}/lap_times") \
.filter(f" as_of_date = '{v_as_of_date}' ") 

qualifying_df = spark.read.format("delta").load(f"{processed_folder_path}/qualifying") \
.filter(f" as_of_date = '{v_as_of_date}' ")

# COMMAND ----------

# MAGIC %md
# MAGIC #-----------------------------------Merge--------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC # Apply the joins

# COMMAND ----------

# MAGIC %md
# MAGIC ###first races and circuites , as both has common column

# COMMAND ----------

# here data is stored in the data frame and later display
race_circuit_join_df = races_df.join(circuits_df,races_df.circuit_id == circuits_df.circuit_id,"inner" ) \
.select(races_df.race_id, races_df.race_year , races_df.race_name , races_df.race_date , circuits_df.circuit_location )
race_circuit_join_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###second result of above with results database + join of the drivers and constructor

# COMMAND ----------

# here data is stored in the data frame and later display
join_df = results_df.join(race_circuit_join_df,results_df.race_id == race_circuit_join_df.race_id,"inner" ) \
                    .join(drivers_df,results_df.driver_id == drivers_df.driver_id,"inner" ) \
                    .join(constructor_df,results_df.constructor_id == constructor_df.constructor_id,"inner" ) \
.select(race_circuit_join_df.race_id,race_circuit_join_df.race_year,race_circuit_join_df.race_name,race_circuit_join_df.race_date,race_circuit_join_df.circuit_location,drivers_df.driver_name,drivers_df.driver_number,drivers_df.driver_nationality,constructor_df.team,results_df.grid,results_df.fastest_lap,results_df.race_time,results_df.points,results_df.position )
join_df.display()

# COMMAND ----------

from pyspark.sql.functions import current_timestamp , col, concat , lit
final_df = add_ingestion_date(join_df).withColumnRenamed("ingestion_date","created_date").withColumn("as_of_date",lit(v_as_of_date))

# COMMAND ----------

# MAGIC %md
# MAGIC #--------------------------------TEST-----------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC # Test the output columns to match with Dashboard column

# COMMAND ----------

# Test the data is coming before write
display(final_df.filter("race_year = 2020 and race_name = 'Abu Dhabi Grand Prix'").orderBy(final_df.points.desc()))

# COMMAND ----------

# MAGIC %md
# MAGIC #----------------------------------WRITE---------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC # Write the results for the future reference and apply all the filteration and analysis

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python but no table creation

# COMMAND ----------

# full load with file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_id').parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Data Lake + Table Creation

# COMMAND ----------

# Write the output of the presentation_db data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as presentation_db used the mounted path
# full load with table and file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_id').format("parquet").saveAsTable("presentation_db.dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write data using python + Delta Lake + Table Creation 

# COMMAND ----------

# Write the output of the presentation_db data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as presentation_db used the mounted path
# full load with table and file creation.
#
# final_df.write.mode("overwrite").format("delta").saveAsTable("presentation_db.dashboard_results")

# COMMAND ----------

# MAGIC %md
# MAGIC ## READ the Solution 1 and Solution 2 from the "injection/5.ingest_results_file.json"
# MAGIC ## Here Solution 2 with function is implemented

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
#
# overwrite_partition_data(final_df,'presentation_db','dashboard_results','race_id')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

# The driver_name cannot be the primary key but the combination of the driver_name and race_id makes the unique record. Becuase as per the data, each race has unique driver name. 
# The race_id is supporting for the partition but here in our case its conributing for the Priamry key Uniqueness also ( so lucky )
input_db="presentation_db"
input_table="dashboard_results"
partition_id="race_id"
primary_key="target.driver_name = source.driver_name AND target.race_id = source.race_id"
merge_delta_data(final_df,input_db,input_table,presentation_folder_path,partition_id,primary_key)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain SQL Read

# COMMAND ----------

# MAGIC %sql
# MAGIC select as_of_date,count(*) from presentation_db.dashboard_results group by as_of_date;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Plain Python read

# COMMAND ----------

# df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")
# df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

#df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")
#df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results/")
df.display()
