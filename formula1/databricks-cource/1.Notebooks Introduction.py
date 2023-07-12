# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook Introduction
# MAGIC ## GUI Introduction
# MAGIC ### Magic Commands
# MAGIC - %python-> Python Language
# MAGIC - %sql   -> SQL Language
# MAGIC - %scala -> Scala Language
# MAGIC - %r     -> R Language
# MAGIC - %fs    -> file system
# MAGIC - %sh    -> shell command
# MAGIC - %md    -> mark down
# MAGIC 
# MAGIC ####### The more details about the md documentation is defined here : https://www.markdownguide.org/cheat-sheet/#basic-synta

# COMMAND ----------

# MAGIC %python
# MAGIC message = 'Welcome to the Notebook'
# MAGIC print(message)

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Welcome to the Notebook"

# COMMAND ----------

# MAGIC %scala
# MAGIC val message = "Welcome to the Notebook"
# MAGIC print(message)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %sh
# MAGIC ps