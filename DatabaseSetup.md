# 1. Database Model

The below tutorial explains the conceptual model of the database used in the proposed solution for storing the trash level in different bins. 

## 1.1  Conceptual Model

The ** E-R Model** below illustrates the key entities and their relationship. This model is later used to design the schema of the database using Postgres SQL via pgAdmin console.

![alt text][logo]

[logo]: /pictures/database/ERModel.png "E-RModel"

The above diagram shows the main entities of the database namely,
* Bin
* Location
* Device
* SensorData
* TransmissionData

As it can be seen in the figure, there can be **n** bins at any location. Therefore, the relation between location and bin is **one-to-many**. Similarly, each bin holds a unique embedded device and therefore the relationship between them is **one-to-one**.

All the readings from the sensor is stored in **SensorData** entity.