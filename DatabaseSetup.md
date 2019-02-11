
# 1. Database Model

The below tutorial explains the conceptual model of the database used in the proposed solution for storing the trash level in different bins. 

## 1.1  Conceptual Model

The **E-R Model** below illustrates the key entities and their relationship. This model is later used to design the schema of the database using Postgres SQL via pgAdmin console.

![alt text][logo]

[logo]: /pictures/database/ERModel.png "E-RModel"

The above diagram shows the main entities of the database namely,
* Bin
* Location
* Device
* SensorData
* TransmissionData

As it can be seen in the figure, there can be **n** bins at any location. Therefore, the relation between location and bin is **one-to-many**. Similarly, each bin holds a unique embedded device and therefore the relationship between them is **one-to-one**.

All the readings from the sensor is stored in **SensorData** entity. The **TransmissionData** entity holds the deserialised data from SensorData.

## 1.2 Setting up the database environment

**pgAdmin** console is used for the the administration of **PostgresSQL** database and can be downloaded at this [link](https://www.pgadmin.org/download/). 

### 1.2.1 Connect to the server

Follow these steps to connect to PostrgesSQL server from the console.

* Launch **pgAdmin** console.
* Click on `Add New Server` from the dashboard.
	
	![alt text][add]
	
	[add]: /pictures/database/AddNewServer.png "Add New Server"
* Select the `connection` tab in the Create Server window and configure it as below,
	![alt text][create]
	
[create]: /pictures/database/CreateServer.png "Create New Server"
* Click `Save` and  Navigate to the “Dashboard” tab and find the state of the server in the “Server activity” section:
	![alt text][server]
	
[server]: /pictures/database/SessionState.png "Server Activity"
* check that the connection between pgAdmin 4 and the PostgreSQL database server is active.

### 1.2.2 Create database schema

* Connect to the target database on the server.
* Under `Schemas` ---> `Tables`, right click and choose `Create - Table` option:
	![alt text][table]
	
[table]: /pictures/database/CreateTable.png "Create Table"

* Choose the appropriate datatype for each column from the dropdown and assign accordingly
* Choose a column for `primary key` which is unique.
	![alt text][primarykey]
	
[primarykey]: /pictures/database/PrimaryKey.png "Primary Key"
* Enforce `foreign key` constraint on any table using the below tab option in `Create Table`.
	![alt text][foreignKey]
	
[foreignKey]: /pictures/database/ForeignKey.png "Foreign Key"

### 1.2.3 Class Diagram
Below diagram shows the class diagram of the solution with different tables (entities) and their columns (attributes).

![alt text][classDiagram]
	
[classDiagram]: /pictures/database/ClassDiagram.png "Class diagram"

The same can be replicated using the steps described above.

### 1.2.4 Alter column datatype

If the column datatype needs to be changed at a later stage, use the below **Data Definition Language(DDL)**:

```SQL
alter table TABLE_NAME alter column COLUMN_NAME NEW_DATATYPE
```
##

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU2MzA1NDEwOCwtNzkyODg5OTYzLC02MD
U3NzQ3NjcsLTQwMTAzNzc0MiwtMjQwNDI4OTY2LDcxNTMwMDQ4
Miw1Nzg1NzQ2NjZdfQ==
-->