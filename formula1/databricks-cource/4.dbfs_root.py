# Databricks notebook source
# MAGIC %md
# MAGIC - the file store does not allowed the comment # in the same cell
# MAGIC - Filestore prepared only when file file manual file gets uploaded in the Databricks via Upload GUI in the Home page.
# MAGIC - The upload file with table creation makes the new table. the table gets created in the default database. The Home -> Data -> Section shows the data of the tables.
# MAGIC - The table can also prepared from the notebook also.

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %fs
# MAGIC ls FileStore/tables/

# COMMAND ----------



# COMMAND ----------

