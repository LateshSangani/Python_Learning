# Databricks notebook source
# MAGIC %md
# MAGIC #### inside include/configuration

# COMMAND ----------

# MAGIC %md
# MAGIC ### Folder path Using Azure Active Directory Access

# COMMAND ----------

# If the mount is NOT availble and azure active directory Access is MISSING then to make authenticate with ADLS then below variable defination is required.
raw_folder_path = "abfss://raw@datasourceformula1.dfs.core.windows.net"
processed_folder_path = "abfss://processed@datasourceformula1.dfs.core.windows.net"
presentation_folder_path = "abfss://presentation@datasourceformula1.dfs.core.windows.net"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Folder path Using Mount point stored createndtials

# COMMAND ----------

# Define the variable where its value is repetivie used across multiple source code file.
raw_folder_path = "/mnt/datasourceformula1/raw"
processed_folder_path = "/mnt/datasourceformula1/processed"
presentation_folder_path = "/mnt/datasourceformula1/presentation"

# COMMAND ----------

display("raw_folder_path : ", raw_folder_path)

# COMMAND ----------

display("processed_folder_path : " , processed_folder_path)

# COMMAND ----------

display("presentation_folder_path : ", presentation_folder_path)
