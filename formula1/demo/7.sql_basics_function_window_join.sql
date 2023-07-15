-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Basics SQL ex: WHERE , GROUP BY , ORDER BY , HAVING 

-- COMMAND ----------

SHOW DATABASES;

-- COMMAND ----------

SELECT CURRENT_DATABASE()

-- COMMAND ----------

SHOW TABLES IN raw_db;

-- COMMAND ----------

--default display of the records is 1000, but for analyis purpose keep the number less for the less computation.
select * from raw_db.circuits limit 10;
select * from raw_db.races limit 10;
select * from raw_db.constructor limit 10;
select * from raw_db.drivers limit 10;
select * from raw_db.results limit 10;
select * from raw_db.pit_stops limit 10;
select * from raw_db.lap_times limit 10;
select * from raw_db.qualifying limit 10;

-- COMMAND ----------

SHOW TABLES IN processed_db;

-- COMMAND ----------

--default display of the records is 1000, but for analyis purpose keep the number less for the less computation.
select * from processed_db.circuits limit 10;
select * from processed_db.races limit 10;
select * from processed_db.constructor limit 10;
select * from processed_db.drivers limit 10;
select * from processed_db.results limit 10;
select * from processed_db.pit_stops limit 10;
select * from processed_db.lap_times limit 10;
select * from processed_db.qualifying limit 10;

-- COMMAND ----------

SHOW TABLES IN presentation_db;

-- COMMAND ----------

--default display of the records is 1000, but for analyis purpose keep the number less for the less computation.
select * from presentation_db.dashboard_constructor limit 10;
select * from presentation_db.dashboard_results limit 10;
select * from presentation_db.dashboard_standings limit 10;

-- COMMAND ----------

--desc <DBNAME>.<TABLE_NAME>;

-- COMMAND ----------

--apply row filter with WHERE
--apply column filer with selected colummns
--do rename of the short acronym columns
--do sorting in descending
select dob as date_of_birth ,name 
from processed_db.drivers 
where nationality = 'British' 
and dob > '1990-01-01'
order by dob desc ;

-- COMMAND ----------

select *
from  processed_db.drivers
order by nationality ASC, dob DESC;

-- COMMAND ----------

select dob , name , nationality
from  processed_db.drivers
where (nationality = 'British' and dob > '1990-01-01') or nationality = 'Indian'
order by dob desc

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # SQL Aggregrate Functions

-- COMMAND ----------

select nationality,count(*) as total_count,max(dob) as min_dob , min(dob) as max_dob , avg(number) as avg_number, sum(number) as sum_number
from  processed_db.drivers
group by nationality

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # GROUP BY and HAVING

-- COMMAND ----------

select nationality,count(*)
from processed_db.drivers
group by nationality
having count(*) > 100
order by nationality;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # SQL Functions

-- COMMAND ----------

select concat(driver_ref,'-',code) as new_driver_ref
from processed_db.drivers;

-- COMMAND ----------

select name,
dob,
split(name,' ') , 
split(name,' ')[0] as first_name, 
split(name,' ')[1] as last_name , 
date_format(dob,'dd-MM-yyyy') as data_of_birth,  --stored formate is YYYY-MM-DD
date_format(date_add(dob,365),'dd-MM-yyyy') as dob_modified, 
current_timestamp() as datatime
from processed_db.drivers;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # SQL Windowing Functions ex: RANK,DENSE_RANK,ROW_NUMBER

-- COMMAND ----------

select nationality , dob , name , rank() over(partition by nationality order by dob desc) as age_rank
from processed_db.drivers
order by nationality,age_rank

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # SQL JOINS

-- COMMAND ----------

SELECT * FROM presentation_db.dashboard_standings;

-- COMMAND ----------

CREATE OR REPLACE VIEW presentation_db.v_driver_standings_2018
AS
SELECT * FROM presentation_db.dashboard_standings
where race_year = 2018;

-- COMMAND ----------

CREATE OR REPLACE VIEW presentation_db.v_driver_standings_2020
AS
SELECT * FROM presentation_db.dashboard_standings
where race_year = 2020;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### INNER JOIN

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### LEFT OUTER JOIN

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
left join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### RIGHT OUTER JOIN

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
right join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### FULL OUTER JOIN

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
full join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### FULL OUTER JOIN WITH UNION

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
left join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)
UNION
select *
from presentation_db.v_driver_standings_2018 d_2018
right join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### SEMI JOIN   -> Inner join but only left table column name output will comes up

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
semi join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###  ANTI JOIN : Inner Join + Over data of the Left table i.e. presentation_db.v_driver_standings_2018

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
anti join presentation_db.v_driver_standings_2020 d_2020
ON (d_2018.driver_name = d_2020.driver_name)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### ANTI JOIN Equivalent with NOT EXISTS Clause

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
where not exists( select 1 from presentation_db.v_driver_standings_2020 d_2020
where d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### CROSS JOIN

-- COMMAND ----------

select *
from presentation_db.v_driver_standings_2018 d_2018
cross join presentation_db.v_driver_standings_2020 d_2020
