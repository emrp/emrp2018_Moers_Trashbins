This Github page contains the documentation and codebase of the project *"Smart Cities: Internet of Waste Bins with LoRa"*. The project is an effort of the students in the study course Emvironmental Monitoring 2018 at Hochschule Rhein-Waal in collaboration with [ ENNI ](https://www.enni.de/) to:

- develop prototype sensor devices installable to the trash bins in ![Moers city](https://goo.gl/maps/PNQHTnw3Vcm) to measure the trash level and wirelessly transmit data of all trash bins to a central location, 
- establish a geo-database system to store and visualize data, and
- research into how trash can be picked up in different locations efficiently and cost-effectively given the information from the sensor devices.
---


- [1. Introduction](#1-introduction)
  * [1.1 Problem Statement](#11-problem-statement)
  * [1.2 Overview](#12-overview)
- [2. Technology Review](#2-technology-review)
  * [2.1 LPWAN](#21-lpwan)
  * [2.2 LoRa](#22-lora)
  * [2.3 LoRaWan](#23-lorawan)
  * [2.4 Time-of-Flight (ToF) Sensors](#24-time-of-flight--tof--sensors)
- [3. Requirements Gathering](#3-requirements-gathering)
- [4. Methodology](#4-methodology)
- [5. Conclusion](#6-conclusion)

### 1. Introduction

Waste is one of the burden issues throughout the world which consequently impacts the environment and to some extent also poses an adverse effect on human health. Waste management is a challenging task to carry out which consists of collection, transport, treatment, and proper disposal and these tasks are followed one after the other in a structural manner for the proper waste management.

  

In the near future, concept of the smart cities will integrate with technology, that will have connectivity and communication to transmit data. Consequently which helps in the process of waste management such as optimising the routes that waste collector vehicles follow for waste collection and removal, together with automating operations with sensors on waste bins signalling that collection is needed when the bins are full. The data from the sensor can transmit information in real-time to a control information system which facilite with Internet of things. Then that redirect route for the collection to the driver and bins to empty. And along with traffic situations and estimated time for collection. After the bins are collected, then information of the waste types can be analysed to determine for the identification of the waste, for example, which bins need to redirect to recycling centres or to disposal centres. So, that will automate the overall process of waste management[1].

  

With the integration with [ ENNI ](https://www.enni.de/), who takes responsibility for the waste management of the Moers city. For the concern on a collection of waste around 11000 waste bins are situated through the Moers city. As from their information, there is a lot of effort and time consuming to identify and collect the waste.

  
  
#### 1.1 Problem Statement

  

On regarding of collection of waste, quite difficult to identify the waste bins are full or not. All the waste bin is not possible to full at the same time and there is the possibility of a single waste bin is full in a wide area where multiple waste bins are located. Along with that some area waste bin full in a shorter period of time while some area waste bin full in a longer period of time. So that requires more time and effort for the waste collector to empty the waste bin.

  
  
  

#### 1.2 Overview

  

Waste Bin integrated with a sensor which measures the height of the waste bin that helps to identify whether the waste is full or not. And along with that find the shortest path for the waste collector to empty the waste bin. So, that reduces time and effort for waster collector to drive through and collect the waste.

  

Initiation of the project with a selection of the appropriate sensor. Among the different sensor, on the basis of portability and accuracy, we select VL53L0X sensor. Consequently, needs a microcontroller board, on that behalf, ESP32 with Lora board is selected and so that makes possible wireless transmission of data from the sensor to the Internet. For receiving the data from Lora WLAN, The Things Network (TTN) is configured in such that established connection with the microcontroller. And the with integration with MQTT, that helps to extract the data from TTN to Database. So that subsequently Postgres Database is configured in such a way that able to store data from sensors. For the case of visualization, GeoServer helps to display with location a waste bins along with latitude and longitude, And having the capability of indication of waste present in the waste bin.


![alt text][logo]

[logo]: /pictures/introduction/system_overview.jpg "Overview"
  
  
### 2. Technology Review

#### 2.1 LPWAN

LPWAN (Low Power Wide Area Network) is a type of wireless technology designed for transmission of small data packages over long distances. LPWAN is well-suited for IoT applications that prioritize low power consumption and wide geographic coverage over data rate, package size and real-time strictness. The figure below demonstrates LPWAN’s range and data rate characteristics compared to other wireless technologies.

|![LWPAN range](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/master/pictures/sensor_node_ttn/lpwan_range.jpg)|
|:--:| 
| *LPWAN Range and Data Rate (Mekki et al. 2018). [Source](https://www.sciencedirect.com/science/article/pii/S2405959517302953)* |

LPWAN is categorized in two different types:

 - Cellular: uses licensed cellular frequencies
 - Non-cellular: uses unlicensed industrial, scientific and medical
   (ISM) radio bands.

Within the scope of this application, only non-cellular LPWAN is concerned. There are several competing technologies under the non-cellular LPWAN umbrella such as:

 - Narrowband IoT (NB-IoT)
 - Sigfox
 - LoRa
 - Weightless

#### 2.2 LoRa

LoRa (Long-Range) is the physical layer of a modulation technique based on chirp spread spectrum (CSS) technology and is a trademark of Semtech Corporation. Beside manufacturing its own LoRa-capable hardware, Semtech also licenses LoRa intellectual property to other manufacturers.

Two typical types of LoRa hardware are:

 - LoRa gateway: acts as a bridge between end nodes and the network
   server (e.g The Things Network server). A LoRa gateway consists of a
   LoRa concentrator board (e.g: IMST iC880A ) and a microcontroller or
   a single-board computer (e.g: Raspberry Pi). LoRa gateways are mostly
   mains-powered and can listen to multiple frequencies silmutaneously.
   
 - LoRa endnode: consists of a LoRa transceiver and a microcontroller. A
   typical LoRa endnote is battery-powered and has sensors connected to
   its microcontroller depending on the application.

#### 2.3 LoRaWan

LoRaWan the datalink layer (colored with blue in the figure below) associated with LoRa. The specification for LoRaWan is open-source and is maintained by the LoRa Alliance. LoRaWan helps determine the nodes lifetimes, network capacity, quality of service, security, and applications served by the network. [from *[A technical overview of LoRa® and LoRaWAN](https://lora-alliance.org/sites/default/files/2018-04/what-is-lorawan.pdf)* by the LoRa Alliance].

| ![LoRaWan layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/master/pictures/sensor_node_ttn/lora_lora_wan_layers.jpg) |
|:--:|
|*LoRa and LoRaWAN Layers LoRa Alliance 2015). [Source](https://lora-alliance.org/sites/default/files/2018-04/what-is-lorawan.pdf)*|

#### 2.4 Time-of-Flight (ToF) Sensors

A ToF sensor is a sensor that:

- Emits a signal (from a light source) to the object  
- Receives the reflected signal (e.g. with a photodiode), then  
measures either the time difference or phase shift in between to determine the distance between the sensor itself and the object.

The VL53L0X Time-of-Flight sensor is used in this application. This sensor utilizes a Vertical Cavity Surface-Emitting Laser (VCSEL) for emitting signals. Compared to ToF sensors that use ultrasonic waves to emit signals, VCSEL-based ToF sensors have a smaller maximum range of measurement. VCSEL-based ToF sensors, however, hold many advantages over ultrasonic ToF sensors:

 - Smaller footprint
   
 - More stable (with respect to laser wavelength)
   
 - Higher resolution
   
 - More accurate thanks to the more focused emitting laser pulses

The height of the trash bins in Moers is less than 1 meter which is well within the measurement range of VCSEL-based ToF sensors, particularly in this case the VL53L0X.

For a more detailed explanation of ToF sensors, refer to [this document](https://www.st.com/content/dam/technology-tour-2017/session-1_track-4_time-of-flight-technology.pdf) by *John Kvam* from STMicroelectronics.

### 3. Requirements Gathering 

The initial phase of the project began with gathering the **requirements** from the project stakeholders. This included the **specifications** of the bin and the **locations** at which the bin is placed. 
Below are few requirements collected during this phase,
- **Bin shape and size**

The following picture describes the width, height and specifications of the bin.

|![bin specs](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/master/pictures/requirements/Bin_Image.PNG)|
|:--:|

- **Map of Moers city**

The map of Moers city were provided to identify the locations of the bin and georeference it in QGIS.

![alt text][map]

[map]: /pictures/requirements/moers_map.png "Map of the city"

- **Bin Locations**

Later, an excel file with information pertaining to the address of each bin with location co-ordinates were provided. This helped in geo-referencing the bins using location coordinates. The `.xls` file was imported in database using scripts and later converted into shapefiles for geoserver.

  [Location of the bins](/Info.csv)

### 4. Methodology 

- [4.1 Sensor Node](/documentation/from_sensor_to_ttn.md)
- [4.2 MQTT](/documentation/MQTT_Data_Handling.md)
- [4.3 Database](/documentation/DatabaseSetup.md)
-  4.4 Georeferencing
    - [4.4.1 Installation](/documentation/GeoReferencing_installation.md)
    - [4.4.2 Implementation](/documentation/Implementation_Georeferencing.md)
- 4.5 Geoserver
    - [4.5.1 Installation](/documentation/GeoServer_installation.md)
    - [4.5.2 Implementation](/documentation/Implementation_GeoServer.md)
    - [4.5.3 Shortest Distance](/documentation/ShortestPathDistance.md)
- [4.6 Visualisation](/documentation/visualisation.md)
- [4.7 Test data creation](/documentation/dummy_data_using_logistic_growth_function.md)

### 5. Conclusion

The end nodes could reliably transmit data to the TTN server while falling back to sleep mode between transmissions. As of 17.02.2019 there are three end node devices periodically transmitting data to the TTN server.
A database model was designed to properly populate data into the Postgres database.
A Python application for getting data from the TTN server with MQTT and storing data to a Postgres database was also implemented.
As ENNI initially provided the project group with a raster map, georefencing was used to map the bin locations from the photo onto actual geographical coordinates. A .csv file with coordinates of the bins was provided later and thus GeoServer was set up to display spatial data that was supposed to be received from the bin location.
A method for calculating the shortest path to collect all the full trash bins was also tested using QGIS and its vector analsysis tool. 
As actual data was not enough in volumn, dummy data was populated into the database using logicstic growth.

As the project involves different fields of study including embedded systems, geoinformatics, database programming and high-level software programming, there were many technical challenges faced. The duration of the course was also a limitation that made the project management process more demanding. Within the scope of this course, certain modules would have been implemented more effectively. On the other hand, due to the project's spanning in many different study areas, it would be less troublesome to separate one module from another and improve the modules individually in the future.
