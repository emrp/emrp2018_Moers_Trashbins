

# emrp2018_Moers_Trashbins

This tutorial explains how to measure the trash level of trashbins using the VL53L0X time-of-flight sensor, Heltec WIFI LoRa 32 (V2) board, The Things Network (TTN) and ... database.

****1. Introduction****

Waste is one of the burden issues throughout the world which consequently impacts the environment and to some extent also poses an adverse effect on human health. Waste management is a challenging task to carry out which consists of collection, transport, treatment, and proper disposal and these tasks are followed one after the other in a structural manner for the proper waste management.

  

In the near future, concept of the smart cities will integrate with technology, that will have connectivity and communication to transmit data. Consequently which helps in the process of waste management such as optimising the routes that waste collector vehicles follow for waste collection and removal, together with automating operations with sensors on waste bins signalling that collection is needed when the bins are full. The data from the sensor can transmit information in real-time to a control information system which facilite with Internet of things. Then that redirect route for the collection to the driver and bins to empty. And along with traffic situations and estimated time for collection. After the bins are collected, then information of the waste types can be analysed to determine for the identification of the waste, for example, which bins need to redirect to recycling centres or to disposal centres. So, that will automate the overall process of waste management[1].

  

With the integration with [ ENNI ](https://www.enni.de/), who takes responsibility for the waste management of the Moers city. For the concern on a collection of waste around 11000 waste bins are situated through the Moers city. As from their information, there is a lot of effort and time consuming to identify and collect the waste.

  
  
****1.1 Problem Statement****

  

On regarding of collection of waste, quite difficult to identify the waste bins are full or not. All the waste bin is not possible to full at the same time and there is the possibility of a single waste bin is full in a wide area where multiple waste bins are located. Along with that some area waste bin full in a shorter period of time while some area waste bin full in a longer period of time. So that requires more time and effort for the waste collector to empty the waste bin.

  
  
  

****1.2 Overview****

  

Waste Bin integrated with a sensor which measures the height of the waste bin that helps to identify whether the waste is full or not. And along with that find the shortest path for the waste collector to empty the waste bin. So, that reduces time and effort for waster collector to drive through and collect the waste.

  

Initiation of the project with a selection of the appropriate sensor. Among the different sensor, on the basis of portability and accuracy, we select VL53L0X sensor. Consequently, needs a microcontroller board, on that behalf, ESP32 with Lora board is selected and so that makes possible wireless transmission of data from the sensor to the Internet. For receiving the data from Lora WLAN, The Things Network (TTN) is configured in such that established connection with the microcontroller. And the with integration with MQTT, that helps to extract the data from TTN to Database. So that subsequently Postgres Database is configured in such a way that able to store data from sensors. For the case of visualization, GeoServer helps to display with location a waste bins along with latitude and longitude, And having the capability of indication of waste present in the waste bin.


![alt text][logo]

[logo]: /pictures/introduction/system_overview.jpg "Overview"
  
  
### 2. Technology Review

#### 2.1 LPWAN

LPWAN (Low Power Wide Area Network) is a type of wireless technology designed for transmission of small data packages over long distances. LPWAN is well-suited for IoT applications that prioritize low power consumption and wide geographic coverage over data rate, package size and real-time strictness. The figure below demonstrates LPWAN’s range and data rate characteristics compared to other wireless technologies.

|![LWPAN range](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/master/pictures/sensor_node_ttn/lpwan_range.jpg)|
|:--:| 
| *Image from a [paper](https://www.sciencedirect.com/science/article/pii/S2405959517302953)* by Kais Mekkia et al.|

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
|*Image by the LoRa Alliace. [[Source]](https://lora-alliance.org/sites/default/files/2018-04/what-is-lorawan.pdf)*|

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

###3. Requirements Gathering

###4. Methodology

[4.1 Technology Overview](/documentation/technology_overview)
[4.1 Sensor Node](/documentation/from_sensor_to_ttn)
[4.2 MQTT](/documentation/MQTT_Data Handling)
[4.3 Database](/documentation/DatabaseSetup)
[4.5 Georeferencing](/documentation/Georeferencing)
[4.6 Geoserver](/documentation/Geoserver)



References

1. Nick Mannie -- https://www.aurecongroup.com/thinking/thinking-papers/how-internet-of-things-change-waste-management-africa

Requirements and walk through:
1. the library requirements are in requirements.txt file. You can download those requirement using following command in terminal "sudo pip3 install -r requirements.txt"

2. You must have python 3.x version installed.

3. The passwords are removed for security reasons so add yourself.
