# Databricks notebook source
# MAGIC %md
# MAGIC ## Load the initial configuration

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

# MAGIC %md
# MAGIC # Import the functions

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import desc , rank , sum , when , count  ,col , asc

# COMMAND ----------

# MAGIC %md
# MAGIC # Read the Input Presentation Data

# COMMAND ----------

# MAGIC %md
# MAGIC ### First get the list of the race year for the new delta AS_OF_DATE data, as data is being analysed based on the race year. 
# MAGIC ### Why because the aggregation is done based on the race year.
# MAGIC ### the Aggregation should not repeate for the race_year which already passed.
# MAGIC ### As the passed year data will not change anytime in the future.

# COMMAND ----------

# MAGIC %md
# MAGIC #### DATA Lake Way

# COMMAND ----------

#race_years = spark.read.parquet(f"{presentation_folder_path}/dashboard_results") \
#.filter(f" as_of_date = '{v_as_of_date}' ") \
#.select("race_year") \
#.distinct() \
#.collect()

# COMMAND ----------

# MAGIC %md
# MAGIC #### DELTA Lake Way

# COMMAND ----------

race_years = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results") \
.filter(f" as_of_date = '{v_as_of_date}' ") \
.select("race_year") \
.distinct() \
.collect()

# COMMAND ----------

type(race_years)

# COMMAND ----------

# MAGIC %md
# MAGIC ### load the list of all the years data in the new empty list
# MAGIC ### For the first time laod when we will history of all the past data this list is required.
# MAGIC ### For the further AS_OF_DATE we can get the same year data many times
# MAGIC ### that same year data need to re-calculate every time

# COMMAND ----------

race_years_list = []
for i in race_years:
    race_years_list.append(i.race_year)
print(race_years_list)

# COMMAND ----------

type(race_years_list)

# COMMAND ----------

# MAGIC %md
# MAGIC # Read the filter source dataframe derived from the presentation/1.dashboard_results

# COMMAND ----------

input_df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_results") \
.filter(col("race_year").isin(race_years_list))

# COMMAND ----------

# MAGIC %md
# MAGIC # Group the Data First

# COMMAND ----------

# MAGIC %md 
# MAGIC ### first group the data

# COMMAND ----------

dashboard_grouped_df = input_df \
.groupBy("race_year","driver_name","driver_nationality") \
.agg(sum("points").alias("total_points"),
     count(when(col("position") == 1 , True)).alias("wins") )

# COMMAND ----------

# MAGIC %md
# MAGIC ### second test the data

# COMMAND ----------

# test the output  with single year
dashboard_grouped_df.filter("race_year = 2020").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### third apply the window for the Rank

# COMMAND ----------

driver_rank_spec = Window.partitionBy("race_year").orderBy(desc("total_points"),desc("wins"))
final_df = dashboard_grouped_df.withColumn("rank",rank().over(driver_rank_spec))

# COMMAND ----------

final_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Write the results for the future reference and apply all the filteration and analysis

# COMMAND ----------

# full load with file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_year').parquet(f"{presentation_folder_path}/dashboard_standings")

# COMMAND ----------

# Write the output of the processed data in the database tables
# it has 2 benifies , table get created and file also stored in the azure storage account as processed_db used the mounted path
# full load with table and file creation.
#
# final_df.write.mode("overwrite").partitionBy('race_year').format("parquet").saveAsTable("presentation_db.dashboard_standings")

# COMMAND ----------

# MAGIC %md
# MAGIC ## READ the Solution 1 and Solution 2 from the "injection/5.ingest_results_file.json"
# MAGIC ## Here Solution 2 with function is implemented

# COMMAND ----------

# its fine not to capture the output dataframe becuase function has wrote now the data and now output dataframe has no use.
# overwrite_partition_data(final_df,'presentation_db','dashboard_standings','race_year')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution 3 (Delta Lake): Incremental laod ( overwrite ) Complex but Fast Performance (USE DELTA)
# MAGIC ### For the incremenal write with overwrite option is re-runnable but it will delete the old data.

# COMMAND ----------

input_db="presentation_db"
input_table="dashboard_standings"
partition_id="race_year"
primary_key="driver_name"
merge_delta_data(final_df,input_db,input_table,presentation_folder_path,partition_id,primary_key)

# COMMAND ----------

# MAGIC %sql
# MAGIC select  race_year,count(*) from presentation_db.dashboard_standings group by race_year;

# COMMAND ----------

# MAGIC %sql
# MAGIC select  * from presentation_db.dashboard_standings where race_year = 2021;

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DATA Lake read

# COMMAND ----------

# df = spark.read.parquet(f"{presentation_folder_path}/dashboard_standings")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### DELTA Lake read

# COMMAND ----------

# test and confirm the data is stored in the readble format
df = spark.read.format("delta").load(f"{presentation_folder_path}/dashboard_standings/")

# COMMAND ----------

df.display()