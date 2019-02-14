 ****Introduction****
 
Waste is one of the burden issues throughout the world and which consequently impact in the environment and to some extent that poses a adverse effect on human health. The management of waste is a challenging task to carry out which consists of collection, transport, treatment, and proper disposal and these task followed one after other  on the structural manner for the proper waste management.

"In the near future, concept of the smart cities will intregrate with technology, that will have connectivity and communication to transmit data. Consequently which helps in the process of waste management such as optimising the routes that waste collector vehicles follow for waste collection and removal, together with automating operations through sensors on waste bins signalling that collection is needed when the bins are full. The data that this automated process generates can transmit information in real-time to a control centre to guide the driver on routes to take, collection points, bins to uplift, traffic situations, estimated time for collection, and provide analytical information on this process to determine the cost of waste collection per kilometre. After the bins are collected, then information on the waste types can be analysed to determine, for example, which bins need to go to recycling centres or to disposal sites. The information can be used to inform clients and provide clients with invoicing information simultaneously via the cloud"[1].

With the integration with [ ENNI ](https://www.enni.de/), who takes responsibility for the waste management of the Moers city. For the concern on a collection of waste around 11000 waste bins are situated through the Moers city.  As from their information,there is a lot of effort and time consuming to identify and collect the waste.




****Problem Statement****

On regarding of collection of waste, quite difficult to identify the waste bins are full or not. All the waste bin is not possible to full at the same time and there is the possibility of a single waste bin is full in a wide area where multiple waste bins are located. Along with that some area waste bin full in a shorter period of time while some area waste bin full in a longer period of time. So that requires more time and effort for the waste collector to empty the waste bin.



****Overviews****

Waste Bin integrated with a sensor which measures the height of the waste bin that helps to identify whether the waste is full or not. And along with that find the shortest path for the waste collector to empty the waste bin. So, that reduces time and effort for waster collector to drive through and collect the waste.

Initiation of the project with a selection of the appropriate sensor. Among the different sensor, on the basis of portability and accuracy, we select VL53L0X sensor. Consequently, needs a microcontroller board, on that behalf, ESP32 with Lora board is selected and so that makes possible wireless transmission of data from the sensor to the Internet. For receiving the data from Lora WLAN, The Things Network (TTN) is configured in such that established connection with the microcontroller. And the with integration with MQTT, that helps to extract the data from TTN to Database. So that subsequently Postgres Database is configured in such a way that able to store data from sensors. For the case of visualization, GeoServer helps to display with location a waste bins along with latitude and longitude, And having the capability of indication of waste present in the waste bin.


Reference
1. Nick Mannie -- https://www.aurecongroup.com/thinking/thinking-papers/how-internet-of-things-change-waste-management-africa
