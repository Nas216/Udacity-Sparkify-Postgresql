# **Sparkify Project**
Sparkify is a startup that provides music streaming through its application. The business is built up using an application that stores information about the users and their selections. The data is stored in JSON format. The company wants to analyze the users' activities to enhance their recommendations based on these activities. There is an option of running SQL queries over the stored data, however, this option carries drawbacks more than the benefits it provides. For example, accomedating the ever-increasing data would slow down the query and render it unuseful day after another. 
The other option the company has is creating a database that accomedate the stored data and run queries on the database rather than on the JSON files. To do so, the company needs a medeling technique that fits their needs. A STAR schema that has a fact table correlates with some dimension tables would do the job.
The fact table in this schema can be built to facilitate for business analysis requirements. Therefore, the fact table would include attributes to the dimension tables in addition to variables that the company wants to analyze. The dimension tables, however, would include information about the users, songs, artisits, and the time of listening to the songs. 



#### *ETL*:
the first step is to Extract the data from the JSON files, Transform it, and finally Load it into the database.
We have two sources of data: 
- log_data: from which the data of *users* and *time* dimension tables would be extracted.
- songs_data: from which the data of *songs* and *artists* dimension tables would be extracted.
the fact table songplays would then be created using the data from those dimension tables.



#### *Modeling process*:
1. ```sql_queries.py ```: is a python code that contains the SQL queries needed to create the fact and dimension tables, in addition to the other queries needed to populate these tables and run selective queries needed for the analysis, namely: song_select
2. ```create_tables.py```: is a python code that defines the functions needed to create and drop tables in Python using the SQL queries encoded in sql_queries.py
    #### Libraries imported:
     ```python
     import psycopg2
     from sql_queries import create_table_queries, drop_table_queries
     ```
      #### Functions:
      **create_database**: it drops any existed connection to the sparkifydb and creates a new connection.

      **drop_tables**: it drops existed tables.

      **create_tables**: it creates tables accordng to the sql statements in *sql_queries* .
4. ```etl.ipynb```: is a pythonic notebook that reads and processes a single file fro the data source into the already created tables. The importance of this file is that is contains detailed instructions on the ETL processes needed.
5. ```test.ipynb```: is pythonic notebook that contains python codes to test whether the tables are correctley created and populated.
6.```etl.py```: is a pyhton code that reads and processes all files from the data source all at once. 
7. ```Untitled.ipynb```: is a blank pythonic notebook that I use to run the executing codes needed to fulfill the ETL processes



