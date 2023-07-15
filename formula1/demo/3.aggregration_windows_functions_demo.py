# Databricks notebook source
# MAGIC %md
# MAGIC # Load the initial configuration

# COMMAND ----------

# MAGIC %run "../include/configuration"

# COMMAND ----------

# MAGIC %run "../include/common_functions"

# COMMAND ----------

# MAGIC %md
# MAGIC # Read the Input Presentation Data

# COMMAND ----------

input_df = spark.read.parquet(f"{presentation_folder_path}/dashboard_results")

# COMMAND ----------

# reduced to the shorten data set
dashboard_df = input_df.filter("race_year = 2020")

# COMMAND ----------

display(dashboard_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # Build in Aggregragte Functions

# COMMAND ----------

# MAGIC %md
# MAGIC #### To use aggregrate Functions , libarary has to import first

# COMMAND ----------

from pyspark.sql.functions import count,countDistinct,sum,max,min,avg

# COMMAND ----------

# MAGIC %md
# MAGIC #### NOTE : All the column name should be in the single or double quotes else Spark gives the error

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1) Count

# COMMAND ----------

# simpe and easy way
dashboard_df.count()

# COMMAND ----------

# take the count of the all the rows
dashboard_df.select(count('*')).display()


# COMMAND ----------

# take the count of the NOT NULL values of the column
dashboard_df.select(count('race_name')).display()


# COMMAND ----------

# take the count of the distinct race_names
dashboard_df.select(countDistinct('race_name')).display()

# COMMAND ----------

dashboard_df.select('race_name').count()

# COMMAND ----------

# this feature is not present
#dashboard_df.select('race_name').countDistinct()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2) Sum

# COMMAND ----------

dashboard_df.select(sum('points')).display()

# COMMAND ----------

dashboard_df.filter("driver_name = 'Lewis Hamilton'").select(sum('points')).display()

# COMMAND ----------

dashboard_df.filter(" driver_name = 'Lewis Hamilton' ")   \
.select(sum('points'),countDistinct('race_name'))    \
.display()

# COMMAND ----------

# The above output does not shows the meaningful column, hence rename it with valid values
# NOTE : in the above about the  column name is written sum(points) and count(DISTINCT race_name)
# here the single and double quotes are missing and same what we got from the above result , its pasted in the withColumnRenamed
dashboard_df.filter(" driver_name = 'Lewis Hamilton' ")   \
.select(sum('points'),countDistinct('race_name'))    \
.withColumnRenamed("sum(points)","TotalPoints")  \
.withColumnRenamed("count(DISTINCT race_name)","DistinctRaces")  \
.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3) Max

# COMMAND ----------

dashboard_df.select(max('points') , min('points')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4) Min

# COMMAND ----------

dashboard_df.select(max('points') , min('points')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5) Avg

# COMMAND ----------

dashboard_df.select(avg('points')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Group By

# COMMAND ----------

# to get the information of single driver , we dont need to group by but just filter 
dashboard_df.filter("driver_name = 'Lewis Hamilton'") \
.select(sum("points").alias("total_points") , countDistinct("race_name").alias("number_of_races")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### group by with multiple aggregrate function using the agg() method

# COMMAND ----------

# to get the information of all the drivers, we need the group by clause
# the group by clause need the extra function agg() because if we SKIP the agg() direct after "group by" write the sum(), then data gets grouped first and then countDistinct failed as it does not get the input dataframe but input groupped processed data. 
# agg() can use to run the multiple Aggregrgate functions
dashboard_df \
.groupBy("driver_name") \
.agg(sum("points").alias("total_points") , countDistinct("race_name").alias("no_of_races")) \
.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Windowing Function

# COMMAND ----------

dashboard_df = input_df.filter("race_year in (2020,2019)")

# COMMAND ----------

dashboard_grouped_df = dashboard_df \
.groupBy("race_year","driver_name") \
.agg(sum("points").alias("total_points") , countDistinct("race_name").alias("no_of_races"))
display(dashboard_grouped_df)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import desc , rank
# setup the variable driver_rank_spec with all the required partition and order by column
driver_rank_spec = Window.partitionBy("race_year").orderBy(desc("total_points"))
# used the above declare variable in dataframe
dashboard_grouped_df.withColumn("rank",rank().over(driver_rank_spec)).display()

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import desc , rank
# Skip the variable and used the complex logic in the over function, just lift and shift
dashboard_grouped_df.withColumn("rank",rank().over(Window.partitionBy("race_year").orderBy(desc("total_points")))).display()

# COMMAND ----------


