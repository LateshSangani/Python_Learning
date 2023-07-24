-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### Create the External Location for the Folders
-- MAGIC #### 1) Bronze
-- MAGIC #### 2) Silver
-- MAGIC #### 3) Gold

-- COMMAND ----------

--From UI< the external location made with below approch.
--Open the databricks workspace URL -> Data Explorer -> External Location -> ex: databrickscource-ext-storage-location

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###### SQL way to make the external location

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS datasourceformula1ucext_bronze
URL "abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/"
WITH (STORAGE CREDENTIAL `databrickscource-ext-storage-credential`);  
-- this symbole `` used because minus symbol is present , it will be good to put underscore.

-- COMMAND ----------

DESC EXTERNAL LOCATION datasourceformula1ucext_bronze

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.fs.ls("abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/")

-- COMMAND ----------

-- MAGIC %fs
-- MAGIC ls "abfss://bronze@datasourceformula1ucext.dfs.core.windows.net/"

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS datasourceformula1ucext_silver
URL "abfss://silver@datasourceformula1ucext.dfs.core.windows.net/"
WITH (STORAGE CREDENTIAL `databrickscource-ext-storage-credential`);  
-- this symbole `` used because minus symbol is present , it will be good to put underscore.

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS datasourceformula1ucext_gold
URL "abfss://gold@datasourceformula1ucext.dfs.core.windows.net/"
WITH (STORAGE CREDENTIAL `databrickscource-ext-storage-credential`);  
-- this symbole `` used because minus symbol is present , it will be good to put underscore.
