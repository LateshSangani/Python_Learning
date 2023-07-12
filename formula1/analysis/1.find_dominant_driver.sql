-- Databricks notebook source
USE presentation_db;

-- COMMAND ----------

select * from presentation_db.calculated_race_results limit 10;

-- COMMAND ----------

--Find the drivers who played more than 50 races and his/her average points through out his/her  whole carrier.
--Why 50 because the driver who played only 1 race and he won then will come top most in the average but his overall points are less. which is incorrect scenerio. 
--Hence threshold is set
select driver_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points,
sum(calculated_points)/count(1) as derived_average
from presentation_db.calculated_race_results
group by driver_name
having total_races >= 50
order by avg_points desc;

-- COMMAND ----------

--Find out the dominat driver in the Previos decade.
select driver_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where race_year BETWEEN 2011 AND 2020
group by driver_name
having total_races >= 50
order by total_points desc;

-- COMMAND ----------

--Find out the dominat driver in the previos 2 decade before.
select driver_name , 
count(1) as total_races,
sum(calculated_points) as total_points,
avg(calculated_points) as avg_points
from presentation_db.calculated_race_results
where race_year BETWEEN 2001 AND 2010
group by driver_name
having total_races >= 50
order by total_points desc;

-- COMMAND ----------

