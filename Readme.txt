Formual 1:  Details about all the scripts prepared as the part of the project

0) demo : 
It listed all the python and sql scripts syntax with example.

1) set-up folder : 
It listed the Python script to make Azure Gen2 storage account linked to the Azure Databricks and accessable.

2) include folder : 
It listed all the Python files which are requried to load all the uesr developed environment variables and functions.

3) utils folder : 
It listed the SQL Scripts for the DB related operations.

4) injection folder : 
It listed all the python scripts to read the Raw files from Storage account datasourceformula1/raw 
container and processed the data and finally clean data stored in the Storage account datasourceformula1/processed folder.

5) procesed folder : 
It listed all the python scripts to read the Storage account datasourceformula1/processed folder
and make the requried dashboard or user presentation data in the 
Storage account datasourceformula1/presentation folder.
	
6) analysis folder : 
It listed the SQL scripts to make the diffrent representation of the data and different reports of the data	
				
7) raw_db folder : 
raw_db database creation and it listed the SQL script to make the EXTERNAL table to read the Raw data files by the Analyst. 
This are called the Bronze Tables. Also the files data gets stored in the Physical table also pointing to the Azure Storage location only.

8) procesed_db folder : 
processed_db database creation and it listed the SQL script to read the Storage account datasourceformula1/processed
data powered by Physical table for the Analyst. This are called the Silver Tables.

9) presentation_db folder : 
presentation_db database creation it listed the SQL script to read the Storage account datasourceformula1/presentation 
data powered by Physical table for the Analyst. Its called the Gold Tables. 
Fact Tables comes here.


Data details:
1) Dimension Tables : The circutis , races , constructor and driveres are the limited master data and its refreshed occatially.
As races are happening limited events only and cicuites are fixed in the world , team and drivers all most working from many years.
The full data dumps is fine and fast to reload any times
2) Fact Tables : The results , pitstops , laptimes , qualifying are the more incremental data where through out the year many data gets coming.
The incremental data does not overwrite the old data.



Mini Project on Unity Catalog
formula1_unity_catalog

1) setup : folder to make the external connections, catalogs , schema
2) bronze_table_creation : folder to make the external tables of the raw format formula1 files.
3) silver_table_creation : folder to make the managed tables of the derived from the bronze location.
4) gold_table_creation : folder to make the managed tables of the derived from the silver location.