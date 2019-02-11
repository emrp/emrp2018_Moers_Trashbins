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
	
	![alt text][image]
	
	[image]: /pictures/database/AddNewServer.png "Add New Server"
* Select the `connection` tab in the Create Server window and configure it as below,
	![alt text][image]
	
[image]: /pictures/database/CreateNewServer.png "Create New Server"
* Click `Save` and  Navigate to the “Dashboard” tab and find the state of the server in the “Server activity” section:
	![alt text][image]
	
[image]: /pictures/database/CreateNewServer.png "Create New Server"
* check that the connection between pgAdmin 4 and the PostgreSQL database server is active.
	![alt text][image]
	
[image]: /pictures/database/SessionState.png "Session State"