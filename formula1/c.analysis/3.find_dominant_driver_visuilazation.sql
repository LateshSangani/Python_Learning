-- Databricks notebook source
-- MAGIC %python
-- MAGIC html = """<h1 style="color:Black;text-align:center;font-family:Ariel"> Report on Dominant Formula1 Driver </h1>"""
-- MAGIC displayHTML(html)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## The dashboard is prepared for the below Graphs and same can be see from the below URL :  https://adb-2643165434444923.3.azuredatabricks.net/?o=2643165434444923#notebook/3773333655865224/dashboard/373281774929714/present

-- COMMAND ----------

USE presentation_db;

-- COMMAND ----------

select * from presentation_db.calculated_race_results_sql limit 10;

-- COMMAND ----------

select driver_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points,
sum(calculated_points)/count(1) as derived_average,
rank() over(order by avg(calculated_points) desc ) driver_rank
from presentation_db.calculated_race_results_sql
group by driver_name
having total_races >= 50
order by avg_points desc

-- COMMAND ----------

--Find the drivers who played more than 50 races and his/her average points through out his/her  whole carrier.
-- Rank the driver with highest average points with new column
--Why 50 because the driver who played only 1 race and he won then will come top most in the average but his overall points are less. which is incorrect scenerio. 
--Hence threshold is set
--This view or select query is to get the all time rank of the driver 
CREATE OR REPLACE TEMP VIEW v_dominant_driver
AS
select driver_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points,
sum(calculated_points)/count(1) as derived_average,
rank() over(order by avg(calculated_points) desc ) driver_rank
from presentation_db.calculated_race_results_sql
group by driver_name
having total_races >= 50
--order by avg_points desc;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## The SQL is same for all the charts but its visuilization is different

-- COMMAND ----------

-- visivulized the top 10 drivers by Line chart
select
  race_year,
  driver_name,
  count(1) as total_races,
  sum(calculated_points) as total_points,
  avg(calculated_points) as avg_points,
  sum(calculated_points) / count(1) as derived_average
from presentation_db.calculated_race_results_sql
where driver_name in ( select driver_name from v_dominant_driver where driver_rank < 11)
group by race_year,driver_name
order by race_year,avg_points desc;

-- COMMAND ----------

-- visivulized the top 10 drivers by bar chart
-- visivulized the top 10 drivers by Line chart
select
  race_year,
  driver_name,
  count(1) as total_races,
  sum(calculated_points) as total_points,
  avg(calculated_points) as avg_points,
  sum(calculated_points) / count(1) as derived_average
from presentation_db.calculated_race_results_sql
where driver_name in ( select driver_name from v_dominant_driver where driver_rank < 11)
group by race_year,driver_name
order by race_year,avg_points desc;

-- COMMAND ----------

-- visivulized the top 10 drivers by Area chart
select
  race_year,
  driver_name,
  count(1) as total_races,
  sum(calculated_points) as total_points,
  avg(calculated_points) as avg_points,
  sum(calculated_points) / count(1) as derived_average
from presentation_db.calculated_race_results_sql
where driver_name in ( select driver_name from v_dominant_driver where driver_rank < 11)
group by race_year,driver_name
order by race_year,avg_points desc;
