# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets/

# COMMAND ----------

# MAGIC %md
# MAGIC ##### replacement of the %fs with actual package used in the background.
# MAGIC ##### just / represent the root folder.

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

# MAGIC %md
# MAGIC ##### For loop to read each location of the files and print it as record.

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    print(files)

# COMMAND ----------

# MAGIC %md
# MAGIC #####  filter for the folders and skip the files

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    if files.name.endswith('/'):
        print(files)    

# COMMAND ----------

# MAGIC %md
# MAGIC ###### only folder name are visible.  other values can be used in the files are files.size,files.modificationTime,files.path

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    if files.name.endswith('/'):
        print(files.name)

# COMMAND ----------

# MAGIC %md
# MAGIC ###### help on the DB utils package , provide its list of the method supported

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### help on the DB utils package method

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help('ls')

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

dbutils.notbook.help()
