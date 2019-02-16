
#this is a simple extraction of data from TTN(The things network) into our local machine and adding it to our preferred database.


#lirary paho.mqtt implementation for communication
import paho.mqtt.client as mqtt
#json library to handle jason file from ttn
import json
#to perform csv execution on data
import csv
#this library allows to using psql in python
import psycopg2

# this these values can be obtained after adding devices to an application in TTN console section
APPEUI = "70B3D57ED00146CC"
APPID  = "emrp2018"
#due to security reasons i have not put the password here. you can copy paste from ttn
PSW    = 'ttn-account-v2.1QxS-JvgRkqkBGIOvhbQDnyvBNsyCl75tanbVJARH4U'


#Call back functions

# gives connection message
def on_connect(mqttc, mosq, obj,rc):
    #simply prints the status of connection. For example "0" for connection established
    print("Connected with result code:"+str(rc)) 
    # subscribe for all devices of user
    mqttc.subscribe('+/devices/+/up')
    
    

# gives message from device
def on_message(mqttc,obj,msg):
    try:

        #to simply print our topic
        print("topic is ", msg.topic)
        
        #here the original message from TTN that is in json format is decoded into dictionary format
        x = json.loads(msg.payload.decode('utf-8'))
        print(x)

        #Extraction of all these values from the original message as they all are dictionary data type
        payload_raw = (x["payload_raw"])   
        #print("payload_raw is ",payload_raw)     
        port_number = (x["port"])
        hardware_serial_number = (x["hardware_serial"])
        device = (x["dev_id"])
        counter = (x["counter"])
        application_id = (x["app_id"])
        airtime_value = (x["metadata"]["airtime"])
        
        payload_fields = x["payload_fields"]

        #measurement_values = (str(list(payload_fields.keys())))
        datetime = x["metadata"]["time"]

        gateways = x["metadata"]["gateways"]
        
        frequency_value = (x["metadata"]["frequency"])
        data_rate_value = (x["metadata"]["data_rate"])
        modulation_value = (x["metadata"]["modulation"])
        coding_rate_value = (x["metadata"]["coding_rate"])
                        
        #this payload_fileds contain the main data which we are measuring . For example distance, temperature
        payload_fields = x["payload_fields"]

        #these if conditions is used when feeding data to sensor data table as we have currently three devices and to recognize device by hardcoded id
        if device == "emrp2018dev002":
          fetched_deviceId = 504 
        if device == "emrp2018dev006":
          fetched_deviceId = 506
        if device == "emrp2018dev004":
          fetched_deviceId = 505
        
        # print for every gateway that has received the message and extract RSSI
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
            
            # this is optional code if you want to store all the extracted values as backup in .csv format in local drive
            # with open('file.csv', mode='a') as csv_file:
            #     fieldnames = ['device_id', 'counter', 'datetime','gateways','temperature','humidity','distance','snr','longitude','latitude']
            #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #     if csv_file.tell() == 0:
            #         writer.writeheader()
            #     if str(device) == "emrp2018dev002":
            #         temperature = payload_fields["temperature_1"]
            #         humidity = payload_fields["relative_humidity_1"]
            #         writer.writerow({'device_id': device, 'counter': counter, 'datetime': datetime,'gateways': gateway_id,'snr':snr,
            #           'longitude':longitude,'latitude':latitude,'temperature':temperature,'humidity':humidity})
            #     if str(device) == "emrp2018dev006":
            #         distance = payload_fields["digital_out_1"]
            #         writer.writerow({'device_id': device, 'counter': counter, 'datetime': datetime,'gateways': gateway_id,'snr':snr,
            #           'longitude':longitude,'latitude':latitude,'distance':distance})
                


                #this is the code to communicate with our database and insert our extracted data .
            try:
              # i have not used password here due to security reasons. you know what password is ;)
               connection = psycopg2.connect(user="emrp2018",
                                              password="emrp2018!",
                                              host="hsrw.space",
                                              port="5432",
                                              database="emrp2018")
               #allows python code to execute psql  
               cursor = connection.cursor()
                              

               # #insert data into Location Table
               # postgres_insert_query = """ INSERT INTO public."Location" ("Latitude","Longitude","Address")
               # VALUES (%s,%s,%s) RETURNING "Id" """
               # record_to_insert = (latitude,longitude,"Moers")           
               # cursor.execute(postgres_insert_query, record_to_insert)
               # fetched_locationId = cursor.fetchone()[0]
               # connection.commit()
               # count = cursor.rowcount
               # print (count, "Record inserted successfully into  table Location")


               
               # #insert into Sensor table
               # postgres_insert_query = """ INSERT INTO public."Sensor" ("Name","MeasurementValue")
               # VALUES (%s,%s) RETURNING "Id" """
               # record_to_insert = (device,measurement_values)           
               # cursor.execute(postgres_insert_query, record_to_insert)
               # fetched_sensorId = cursor.fetchone()[0]
               # connection.commit()
               # count = cursor.rowcount
               # print (count, "Record inserted successfully into  table Sensor")



               # #insering values into table Device
               # postgres_insert_query = """ INSERT INTO public."Device" ("SensorId") 
               # VALUES (%s) RETURNING "Id" """               
               # record_to_insert = (fetched_sensorId,)
               # cursor.execute(postgres_insert_query, record_to_insert) 
               # fetched_deviceId = cursor.fetchone()[0]              
               # connection.commit()
               # count = cursor.rowcount
               # print (count, "Record inserted successfully into  table Device")


               # #insering values into table Bin
               # postgres_insert_query = """ INSERT INTO public."Bin" ("LocationId","DeviceId") 
               # VALUES (%s,%s) """         
               # record_to_insert = (fetched_locationId,fetched_deviceId)
               # cursor.execute(postgres_insert_query, record_to_insert)
               # connection.commit()
               # count = cursor.rowcount
               # print (count, "Record inserted successfully into  table Bin")



               #insering values into table TTNGateway and atlast returnning the gatewayid
               postgres_insert_query = """ INSERT INTO public."TTNGateway" (gtw_id,timestamp,channel,
               rssi,snr,longitude,latitude,time) 
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING "GatewayId" """
               record_to_insert = (gateway_id,timestamp,channel,rssi,snr,longitude,latitude,time)
               cursor.execute(postgres_insert_query, record_to_insert)
               fetched_gatewayId = cursor.fetchone()[0]
               connection.commit()
               count = cursor.rowcount
               print (count, "Record inserted successfully into  table TTNGateway")




               # #insert into sensor data table
               postgres_insert_query = """ INSERT INTO public."SensorData" ("DeviceId","Level","Battery",app_id,dev_id,hardware_serial,
               port,counter,payload_raw,"time",frequency,modulation,data_rate,airtime,coding_rate,"TTNGatewayId",payload_fields)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING "DataId" """

               record_to_insert = (fetched_deviceId,"23","12",application_id,device,hardware_serial_number,port_number,counter,payload_raw,time,
               frequency_value,modulation_value,data_rate_value,airtime_value,coding_rate_value,fetched_gatewayId,json.dumps(payload_fields))
              
               cursor.execute(postgres_insert_query, record_to_insert)
               fetched_sensorDataId = cursor.fetchone()[0]
               connection.commit()        
               count = cursor.rowcount
               print (count, "Record inserted successfully into  table SensorData")     




               # #insert into TrasmissionData table
               # postgres_insert_query = """ INSERT INTO public."TransmissionData" ("VariableType","VariableValue","SensorDataId")
               # VALUES (%s)"""
               # record_to_insert = (fetched_sensorDataId)
               # cursor.execute(postgres_insert_query, record_to_insert)
               # connection.commit()        
               # count = cursor.rowcount
               # print (count, "Record inserted successfully into  table TransmissionData")         



            #if any exception occurs during database communication
            except (Exception, psycopg2.Error) as error :
                if(connection):
                    print("Failed to insert record into  table", error)
            
            finally:
                #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")


            
    #if any exception occurs during message sending process from TTN
    except Exception as e:
      print(e)
      pass

# def on_publish(mosq, obj, mid):
#     print("mid: " + str(mid),str(mosq),str(obj))
    

# def on_subscribe(mosq, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))

# def on_log(mqttc,obj,level,buf):
#     print("message:" + str(buf))
#     print("userdata:" + str(obj))

#creating object of mqtt client
mqttc= mqtt.Client()

# Assign event callbacks
mqttc.on_connect=on_connect
mqttc.on_message=on_message

#creating connection to the things network 
mqttc.username_pw_set(APPID, PSW)
mqttc.connect("eu.thethings.network",1883)


# and listen to server
run = True
while run:
    mqttc.loop()