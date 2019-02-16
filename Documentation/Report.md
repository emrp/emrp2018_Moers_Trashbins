    ## 1. Introduction

This report is one of the parts of the complete project named as “Moers Trash Bins Using LoRaWAN”. Each student working on this project has their own share of contribution so as mine. In simple terms I was assigned to extract data from thethingsnetwork.org platform (The Things Network is web platform enabling low power Devices to use long range Gateways to connect to an open-source, decentralized Network to exchange data with Applications.) to our local computer and then feed to our database which is a postgres database. The data in thethingsnetwork.org is being sent from our sensors(eg.Distance measuring sensor). Being from software background I was lacking the idea about integrating software and hardwares so our professor Becker gave us the idea of using a very useful messaging protocol called  MQTT for the data extraction. Similarly, I came up with an idea to use psycopg2 for feeding data to our database. The remaining part of this report is all about MQTT and how I was able to implement it.  All the codes are written in python programming language and due to which we were able to use libraries for like mqtt and psycopg2.

<img src = "/Images/simple flow of work.png">

                     Fig : Simple flow of work with mqtt and psycopg2 highlighted

1.1 What is MQTT?

MQTT (Message Queuing Telemetry Transport) is a publish/subscribe messaging protocol designed keeping in mind the purpose of  small devices. Publish/Subscribe systems work like a message bus. We send a message to a topic, and any software with a subscription for that topic gets a copy of our message. As a sender, we never really know who is listening; you just provide our information to a set of topics and listen for any other topics we might care about. It's like walking into a party and listening for interesting conversations to join (Dague, 2018).

“MQTT stands for MQ Telemetry Transport. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for constrained devices and low-bandwidth, high-latency or unreliable networks. The design principles are to minimize network bandwidth and device resource requirements whilst also attempting to ensure reliability and some degree of assurance of delivery. These principles also turn out to make the protocol ideal of the emerging “machine-to-machine” (M2M) or “Internet of Things” world of connected devices, and for mobile applications where bandwidth and battery power are at a premium” (Mqtt.org).
There are several implementations of MQTT. Some of them are Mosquitto, mqtt paho,JoramMQ. For this project , paho MQTT is been used but i have describe Mosquitto implementation as well. 
<img src = "/Images/mqtt.png">

                     Fig: Basic Flow of MQTT function
1.1.1 What is MQTT paho ?

Paho is a MQTT implementation which is available for different programming languages including python. The backend of this project is based on python so the paho mqtt library for python is used. An MQTT client (also called a client application) collects information from a telemetry device,connects to a messaging server, and uses a topic string to publish the information in a way that allows other clients or applications to retrieve it. An MQTT client also can subscribe to topics, receive publications associated with those topics, and issue commands to control the telemetry device. It is available for different programming languages like C, C#, Java, Python, JavaScript.

1.2  What is psycopg2 ?

Psycopg is the most popular PostgreSQL database adapter for the Python programming language. psycopg2 is basically a library which can be used in python code to communicate with postgres database. In this project, psycopg2 plays an important role of feeding all the data from thethingsnetwork.org to our postgres database.

    2. Why we needed MQTT ?

Our project required a protocol which can be used to extract data from platforms like thethingsnetwork.org where we are sending our sensor data directly from the sensors. MQTT enables us to extract data from thethingsnetwork conveniently and efficiently.
According to Lampkin et al., 2012, MQTT is design includes the following underlying principles:

- Simplicity: The protocol was made open so that it can be integrated easily into other solutions.

- Use of a publish/subscribe model: The sender and the receiver are decoupled. Thus, publishers do not need to know who or what is subscribing to messages and vice versa.

- Minimal maintenance: Features, such as automated message storage and retransmission, minimize the need for on-the-fly administration.

- Limited on-the-wire footprint: The protocol keeps data overhead to a minimum on every message.

- Continuous session awareness: By being aware of when sessions have terminated, the protocol can take action accordingly, thanks in part to a will feature.

- Local message processing: The protocol assumes that remote devices have limited processing capabilities.

- Message persistence: Through the designation of specific QoS, the publisher can ensure delivery of the most important messages(Higher QoS levels ensure more reliable message delivery but might consume more network bandwidth or subject the message to delays due to issues such as latency.).

- Agnostic regarding data types: The protocol does not require that the content of messages be in any particular format.


2.1 MQTT vs HTTP

According to Lampkin et al., 2012, although comparison is often made between MQTT and other common protocols, the most useful comparison is with HTTP, for the following reasons:

 - HTTP is the most widely used and available protocol. Almost all computing devices with a TCP/IP stack have it. In addition, because HTTP and MQTT are both based on TCP/IP, developers need to choose between them.
 
 - The HTTP protocol uses a request/response model, which is currently the most common message exchange protocol. MQTT uses a publish/subscribe pattern. Developers need to understand the relative advantages of each type of model

Here is a fuller explanation of the critical differences between the MQTT and HTTP protocols for devices:
  Design orientation
- MQTT is data-centric. It transfers data content as byte array. It does not care about content.

- HTTP is document-centric. It supports the MIME standard to define content type, but constrained devices usually do not need this advanced feature.

 Messaging pattern
- MQTT uses a publish/subscribe messaging pattern that has loose coupling. Clients do not need to be aware of the existence of other devices. They just need to care about the content to be delivered or received.

- HTTP uses a request/response messaging model. It is a basic and powerful messaging exchange pattern, but the client needs to know the address of all devices to which it connects.

 Complexity of protocol
- The MQTT specification is short. It has few message types and only the CONNECT, PUBLISH, SUBSCRIBE, UNSUBSCRIBE, and DISCONNECT types are important for developers.

- HTTP is a more complex protocol, with a specification that is more than 160 pages long. It uses many return codes and methods (such as POST, PUT, GET, DELETE,HEAD, TRACE, CONNECT, and so on). It works well for hypermedia information systems, but constrained devices typically do not need all of its features.

 Message size
- MQTT is designed specifically for constrained devices. It includes only the features that are necessary to support them. The message header in MQTT is short, and the smallest packet size for a message is 2 bytes.

- HTTP uses a text format, not a binary format, which allows for lengthy headers and messages. The text format is readable by humans, which makes the HTTP protocol easy to troubleshoot and has contributed to its popularity. However, this format is more
than is needed, or desirable, for constrained devices with limited computational resources in low-bandwidth network environments.
 
 Quality of Service levels
- MQTT supports three QoS levels in message publication. Developers do not have to implement additional, complex features to ensure message delivery.

- HTTP has no retry ability or QoS features. If developers need guaranteed message delivery, they have to implement it themselves.

 Extra libraries
- MQTT works well on devices with limited memory due, in part, to its small library requirement, only about 30 KB for the C client and 100 KB for the Java client and similar to that for python.
- HTTP does not require any libraries by itself, but additional libraries of parsers for JSON or XML are required if using SOAP- or RESTful-style web services.

 Data distribution
– MQTT includes a built-in distribution mechanism, supporting the 1 to 0, 1 to 1, and 1 to many distribution models.
– HTTP is point-to-point and has no built-in distribution feature. Developers must create their own distribution mechanism or adapt common techniques, such as long-polling.




    3. MQTT paho  and psycopg2 Implementation
    
The backend code is written in python(version 3.x) so it was easier to implement mqtt paho and psycopg2 library in python. All these codes are implemented in Linux OS . But mqtt paho and psycopg2 works well with other OS too. 

3.1 Install mqtt paho and psycopg2

The latest stable version of paho-mqtt is available in the Python Package Index (PyPi) and can be installed using:

    sudo pip install paho-mqtt

For more information : https://www.eclipse.org/paho/clients/python/docs/
Make sure you have pip install. For more information on that please follow the link : https://www.makeuseof.com/tag/install-pip-for-python/

The latest version of psycopg2 can be installed using:

    sudo pip install psycopg2

For more information : http://initd.org/psycopg/docs/install.html

Note : Depending upon the version of python and pip installed, you might need to replace pip with pip3 in case of error or no installation.

3.2 Understanding mqtt with Mosquitto

Mosquitto is a small, no-cost, open source implementation of an MQTT broker that supports the MQTT  protocol. Mosquitto replicates the functionality of Really Small Message Broker.

Install the latest Mosquitto Broker available in Linux Terminal using :

    sudo apt-get install mosquitto
 
The Mosquitto service will start after installation.Then Install MQTT clients using :

    sudo apt-get install mosquitto-clients

For more installation and operation information : 
http://www.steves-internet-guide.com/install-mosquitto-broker/
https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04

Mosquitto clients help us easily test MQTT through a command line utility. We will use two command windows, one to subscribe to a topic named "test" and one to publish a message to it.

To Subscribe to topic "test" we need to enter the following code in one of the two terminals:

    mosquitto_sub -t "test"

Mosquito_sub is a subscribe client . Here we are specifying "-t" followed by a topic name. To Publish a message to topic "test" enter the following code in another terminal:

    mosquitto_pub -m "message from mosquitto_pub client" -t "test"

Here the additional parameter "–m" is followed by the message we want to publish. Hit "Enter" and we should see a message from mosquitto_pub client displayed in other terminal where mosquito_sub client is running.

<img src = "/Images/mosquitto.png">

               Fig: Mosquitto Implementation using two terminals 
               
   <br>

   
    4. Understanding mqtt paho and psycopg2 code
    
The code written for this project is simple yet powerful enough to grab the topic message and manipulate them and finally insert into our postgres database.
4.1 mqtt paho
```python

    #importing library paho.mqtt.client
    import paho.mqtt.client as mqtt

    #creating object of mqtt client
    mqttc= mqtt.Client()

```
- Assign event callbacks
```python

        mqttc.on_connect=on_connect
        mqttc.on_message=on_message

```

Callbacks are functions that are called in response to an event.The events and callbacks for the Paho MQTT client are as follows:

- Event Connection acknowledged Triggers the on_connect callback
- Event Disconnection acknowledged Triggers the on_disconnect callback
- Event Subscription acknowledged Triggers the  on_subscribe callback
- Event Un-subscription acknowledged Triggers the  on_unsubscribe callback
- Event Publish acknowledged Triggers the on_publish callback
- Event Message Received Triggers the on_message callback
- Event Log information available Triggers the on_log callback

```python

        #these values can be obtained after adding devices to an application in TTN console section of thethingsnetwork.org
        APPEUI = "70B3D57ED00146CC"
        APPID  = "emrp2018"
        #due to security reasons i have not put the password here. you can copy paste from ttn
        PSW    = 'ttn-account********************************************'

```

```python
        # listen to server in a loop
        run = True
        while run:
            mqttc.loop()


        #Call back functions
        # gives connection message
        def on_connect(mqttc, mosq, obj,rc):
            #simply prints the status of connection. For example "0" for connection established
            print("Connected with result code:"+str(rc)) 
            # subscribe for all devices of user
            mqttc.subscribe('+/devices/+/up')
```

Output:

    Connected with result code:0

This means the connection is established to the server. Similarly 2 means unauthorized access.  

```python

    #callback function
    # when the message arrives
    def on_message(mqttc,obj,msg):
        try:

            #to simply print our topic
            print("topic is ", msg.topic)

            #here the original message from TTN that is in json format is decoded into dictionary format
            x = json.loads(msg.payload.decode('utf-8'))
            #Extraction of all these values from the original message as they all are dictionary data type
            payload_raw = (x["payload_raw"])   
            port_number = (x["port"])

```

The simple output of the message from thethingsnetwork which is stored in variable ‘x’ will be:

    {'app_id': 'emrp2018', 'metadata': {'modulation': 'LORA', 'frequency': 868.5, 'coding_rate': '4/5', 'airtime': 56576000, 'data_rate': 'SF7BW125', 'time': '2019-02-13T00:10:01.743984477Z', 'gateways': [{'latitude': 51.500282, 'channel': 2, 'rf_chain': 1, 'gtw_id': 'eui-b827ebfffe21faed', 'timestamp': 3155085291, 'longitude': 6.5457115, 'rssi': -112, 'snr': 3.5, 'time': '2019-02-13T00:10:01.721735Z', 'location_source': 'registry'}]}, 'payload_raw': 'AWcA+gFoeA==', 'port': 1, 'counter': 491, 'payload_fields': {'temperature_1': 25, 'relative_humidity_1': 60}, 'hardware_serial': '00726FD9E8775924', 'dev_id': 'emrp2018dev004'}.

Here , the main data which we measured is in payload_filed : 'payload_fields': {'temperature_1': 25, 'relative_humidity_1': 60},

```python

        #this payload_fileds contain the main data which we are measuring . For example distance, temperature
        payload_fields = x["payload_fields"]
        
        # loops for every gateway that has received the message and extract gateway information
        for gw in gateways:

            #inside metadata, we have gateways and inside gateways we have all these below values . they are in dictionary data type as well
            gateway_id = gw["gtw_id"]
            rssi = gw["rssi"]
            snr = gw['snr']
          
            latitude = gw['latitude']
            longitude = gw['longitude']
            time = gw['time']
            timestamp = gw['timestamp']
            channel = gw['channel']

    # Exception if any error occurs during the process
     except Exception as e:
          print(e)

```
   

4.2 psycopg2
 
 ```python

    #this is the code to establish connection with our database and insert our data .
            try:
              # i have not used password here due to security reasons. you know what password is ;)
               connection = psycopg2.connect(user="emrp2018",
                                              password="*******",
                                              host="hsrw.space",
                                              port="5432",
                                              database="emrp2018")
            
       #allows python code to execute psql  
                   cursor = connection.cursor()


            
       #insert data into Location Table
                   postgres_insert_query = """ INSERT INTO public."Location" ("Latitude","Longitude","Address")
                   VALUES (%s,%s,%s) RETURNING "Id" """
                   record_to_insert = (latitude,longitude,"Moers")           
                   cursor.execute(postgres_insert_query, record_to_insert)
                   connection.commit()
                   count = cursor.rowcount
                   print (count, "Record inserted successfully into  table Location")

    #if any exception occurs; to handle it. 
    except (Exception, psycopg2.Error) as error :
                    if(connection):
                        print("Failed to insert record into  table", error)
            
            finally:
                #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")


```
  
    6. Result Images
    
<img src = "/Images/command.png">

                Fig : Result in Terminal to ensure the connection to TTN and  show which tables are affected 
  
  Just to insure that the tables are populated and which table is populated , our the python code is designed with this feature. In case of any error/exceptions it will give an error message so it is easier for us to track the error.
     
<img src = "/Images/sensordata.png">
           
                Fig : Result after feeding data to database using the given code(psycopg2)
This image shows the last result after feeding data successfully into postgres database table.



# References


Dague, S. (2018). Using MQTT to send and receive data for your next project. [online] Opensource.com. Available at: https://opensource.com/article/18/6/mqtt?fbclid=IwAR3CiznOiazYjaqzygYU5_U2aFdglxP54g0zV9nlq16YA19K6Ed9EGGeXcs [Accessed 11 Feb. 2019].

Mqtt.org. FAQ - Frequently Asked Questions | MQTT. [online] Available at: http://mqtt.org/faq [Accessed 11 Feb. 2019].
Lampkin, V., Leong, W., Olivera, L., Rawat, S., Subrahmanyam, N. and 7Xiang, R. (2012). Building Smarter Planet solutions with MQTT and IBM WebSphere MQ Telemetry. 1st ed. [S.l.]: IBM, pp.7-8.
