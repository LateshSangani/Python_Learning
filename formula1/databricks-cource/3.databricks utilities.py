# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

# replacement of the %fs with actual package used in the background.
# just / represent the root folder.
dbutils.fs.ls('/')

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    print(files)

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    if files.name.endswith('/'):
        print(files)
  # all the files skipped only folder remaning      

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/'):
    if files.name.endswith('/'):
        print(files.name)
  # only folder name are visible.  other values can be used in the files are files.size,files.modificationTime,files.path

# COMMAND ----------

#help on the DB utils package , provide its list of the method supported
dbutils.help()

# COMMAND ----------

#help on the DB utils package method
dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help('ls')

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

