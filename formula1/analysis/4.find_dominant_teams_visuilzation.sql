-- Databricks notebook source
USE presentation_db;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC html = """<h1 style="color:Black;text-align:center;font-family:Ariel"> Report on Dominant Formula1 Team </h1>"""
-- MAGIC displayHTML(html)

-- COMMAND ----------

-- MAGIC 
-- MAGIC %md
-- MAGIC ## The dashboard is prepared for the below Graphs and same can be see from the below URL : https://adb-2643165434444923.3.azuredatabricks.net/?o=2643165434444923#notebook/373281774929696/dashboard/373281774929718/present

-- COMMAND ----------

select * from presentation_db.calculated_race_results limit 10;

-- COMMAND ----------

--Find the Team who played more than 100 races ( as team as min 2 drivers ) and his/her average points through out his/her  whole carrier.
--Why 100 because the team who played only 1 race and team won then will come top most in the average but team overall points are less. which is incorrect scenerio. 
--Hence threshold is set
--This view or select query is to get the all time rank of the teams 
CREATE OR REPLACE TEMP VIEW v_dominant_team
AS
select constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points,
sum(calculated_points)/count(1) as derived_average,
rank() over(order by avg(calculated_points) desc ) team_rank
from presentation_db.calculated_race_results
group by constructor_name
having total_races >= 100
--order by avg_points desc;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## SQL is same only charts are different

-- COMMAND ----------

--Find out the top 5 dominat team through the year , line chart
select race_year,constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where constructor_name in ( select constructor_name from v_dominant_team where team_rank < 5)
group by race_year,constructor_name
order by race_year,avg_points desc;

-- COMMAND ----------

--Find out the top 5 dominat team through the year , Area chart
select race_year,constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where constructor_name in ( select constructor_name from v_dominant_team where team_rank < 5)
group by race_year,constructor_name
order by race_year,avg_points desc;

-- COMMAND ----------

