-- Databricks notebook source
USE presentation_db;

-- COMMAND ----------

select * from presentation_db.calculated_race_results limit 10;

-- COMMAND ----------

--Find the Team who played more than 100 races ( as team as min 2 drivers ) and his/her average points through out his/her  whole carrier.
--Why 100 because the team who played only 1 race and team won then will come top most in the average but team overall points are less. which is incorrect scenerio. 
--Hence threshold is set
select constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points,
sum(calculated_points)/count(1) as derived_average
from presentation_db.calculated_race_results
group by constructor_name
having total_races >= 100
order by avg_points desc;

-- COMMAND ----------

--Find out the dominat team in the Previos decade.
select constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where race_year BETWEEN 2011 AND 2020
group by constructor_name
having total_races >= 100
order by total_points desc;

-- COMMAND ----------

--Find out the dominat team in the previos 2 decade before.
select constructor_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where race_year BETWEEN 2001 AND 2010
group by constructor_name
having total_races >= 100
order by total_points desc;

-- COMMAND ----------

