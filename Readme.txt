Formual 1:  Details about all the scripts prepared as the part of the project
1) set-up folder : It listed the Python script to make Azure Gen2 storage account linked to the Azure Databricks 
                   and accessable.
2) include folder : It listed all the Python files which are requried to load all the uesr developed environment variables 
                    and functions.
3) utils folder : It listed the SQL Scripts for the DB related operations.
4) injection folder : it listed all the python scripts to read the Raw files from Storage account databrickscourcedl/raw 
                      container and processed the data and finally clean data stored in the Storage account 
					  databrickscourcedl/processed folder.
5) raw_db folder : it listed the SQL script to make the EXTERNAL table to read the Raw data files by the Analyst. 
                   This are called the Bronze Tables.
6) procesed folder : it listed all the python scripts to read the Storage account databrickscourcedl/processed folder
                     and make the requried dashboard or user presentation data in the 
					 Storage account databrickscourcedl/presentation folder.
					 Also the files data gets stored in the Physical table also pointing to the Azure Storage location only.
7) procesed_db folder : it listed the SQL script to read the Storage account databrickscourcedl/processed 
                        data powered by Physical table for the Analyst. 
                        This are called the Silver Tables.
8) presentation_db folder : it listed the SQL script to read the Storage account databrickscourcedl/presentation 
                            data powered by Physical table for the Analyst. Its called the Gold Tables. 
							Fact Tables comes here.
9) analysis folder : it listed the SQL scripts to make the diffrent representation of the data 
                     and diffrent reports of the data

Suppliment folder :
1) demo : it listed all the python and sql scripts trained by the trainer in the cource.
2) databricks-cource : it listed the python scripts as the utlities provided by the data bricks.