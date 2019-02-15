### Technology Review

#### 1 LPWAN

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

#### 2 LoRa

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

#### 3 LoRaWan

LoRaWan the datalink layer (colored with blue in the figure below) associated with LoRa. The specification for LoRaWan is open-source and is maintained by the LoRa Alliance. LoRaWan helps determine the nodes lifetimes, network capacity, quality of service, security, and applications served by the network. [from *[A technical overview of LoRa® and LoRaWAN](https://lora-alliance.org/sites/default/files/2018-04/what-is-lorawan.pdf)* by the LoRa Alliance].

| ![LoRaWan layer](https://github.com/emrp/emrp2018_Moers_Trashbins/blob/master/pictures/sensor_node_ttn/lora_lora_wan_layers.jpg) |
|:--:|
|*Image by the LoRa Alliace. [[Source]](https://lora-alliance.org/sites/default/files/2018-04/what-is-lorawan.pdf)*|

#### 4 Time-of-Flight (ToF) Sensors

A ToF sensor is a sensor that:

emits a signal (from a light source) to the object  
receives the reflected signal (e.g. with a photodiode), then  
measures either the time difference or phase shift in between to determine the distance between the sensor itself and the object.

The VL53L0X Time-of-Flight sensor is used in this application. This sensor utilizes a Vertical Cavity Surface-Emitting Laser (VCSEL) for emitting signals. Compared to ToF sensors that use ultrasonic waves to emit signals, VCSEL-based ToF sensors have a smaller maximum range of measurement. VCSEL-based ToF sensors, however, hold many advantages over ultrasonic ToF sensors:

 - Smaller footprint
   
 - More stable (with respect to laser wavelength)
   
 - Higher resolution
   
 - More accurate thanks to the more focused emitting laser pulses

The height of the trash bins in Moers is less than 1 meter which is well within the measurement range of VCSEL-based ToF sensors, particularly in this case the VL53L0X.

For a more detailed explanation of ToF sensors, refer to [this document](https://www.st.com/content/dam/technology-tour-2017/session-1_track-4_time-of-flight-technology.pdf) by *John Kvam* from STMicroelectronics.
