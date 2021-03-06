- [1. Database Model](#1-database-model)
  * [1.1  Conceptual Model](#11--conceptual-model)
  * [1.2 Setting up the database environment](#12-setting-up-the-database-environment)
    + [1.2.1 Connect to the server](#121-connect-to-the-server)
    + [1.2.2 Create database schema](#122-create-database-schema)
    + [1.2.3 Class Diagram](#123-class-diagram)
    + [1.2.4 Alter column datatype](#124-alter-column-datatype)
  * [1.3 Master Data](#13-master-data)
    + [1.3.1 Insert Scripts](#131-insert-scripts)
  * [1.4 Primary key generation](#14-primary-key-generation)
  * [1.5 Triggers](#15-triggers)

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
## 1.3 Master Data 

There are certain tables where the data needs to be inserted before the database is functional for the use.
These tables in the database are chosen to be,
+ Bin
+ Location
+ Device

The reason being, the information about the locations of the bins are given to us from the customer. Also, the devices registered in TTN console needs to be registered in the database as well.

### 1.3.1 Insert Scripts

Once, the database schema is setup, the input (.xls) file from the customer is `preprocessed` to adjust it according to the specifications of the database.

Use the below example to construct the insert data script,
```SQL
insert into public."Location" ("Latitude","Longitude","Id","Address") values (51.41055037,6.584027857,1139,'Moers');
```
The scripts are generated for each tables, Bin,Location and Device.

## 1.4 Primary key generation

The `Id` column of each table is usually marked as the `primary key`. To randomly generate the unique ID for each table, below sequence is used:

```SQL
CREATE SEQUENCE id_generation  start 100  increment 1;
```
**Assigning the sequence as DEFAULT to Id column of the fields**
```SQL
ALTER TABLE table_name ALTER COLUMN ID (nextval('id_generation') DEFAULT;
```
## 1.5 Triggers

The data transferred to the database from the sensor node via MQTT is in serialised JSON format. The relevant data is framed under "payload_fields" object which can contain multiple "key-value" pairs denoting information like humidity, precipitation, temperature and the distance from the time-of-flight sensor. All this information is combined into one structure such as,

```JSON
"{
	"relative_humidity_1":31.5,
	"temperature_1":23.2,
	"digital_out_1":0
}"
```
The above information needs to be deserialised and updated in the `TransmissionTable` . To acheive this, a trigger is written in Postgres SQL which is executed on `INSERT` of any rowdata in the table `SensorData`.

The below function uses `json_each` and `json_object_keys` methods to deserialise the data and insert into SensorData table.
```SQL

CREATE FUNCTION public.insert_transmission()
    RETURNS trigger
    AS $BODY$
begin
insert into public."TransmissionData" ("VariableType","VariableValue")
values (json_object_keys(new.payload_fields),
			replace(split_part(cast(json_each(new.payload_fields) as text),',',2),')','')
	   );
	return new;
end
$BODY$;
```
The above function is called when the trigger is executed as below,
```SQL
CREATE TRIGGER insert_transmission_trigger
    AFTER INSERT
    ON public."SensorData"
    FOR EACH ROW
    EXECUTE PROCEDURE public.insert_transmission();
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2OTgxMDYzNTYsMzY1NDk2MjY3LC05OD
U5MDQ2MzIsNTIyNjkzNDY0LDExNjA0Mzc2NzQsODk0NzEzNjkz
LC00NDMxMDExMjAsLTc5Mjg4OTk2MywtNjA1Nzc0NzY3LC00MD
EwMzc3NDIsLTI0MDQyODk2Niw3MTUzMDA0ODIsNTc4NTc0NjY2
XX0=
-->