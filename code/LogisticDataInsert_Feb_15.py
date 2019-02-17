import numpy as np
import matplotlib.pyplot as plt
import time
import psycopg2
from pprint import pprint
payload_fields='{"level":"2.4"}'

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection= psycopg2.connect(
			"dbname='emrp2018' user='emrp2018' host='hsrw.space' password='emrp2018!'")
			self.connection.autocommit=True
			self.cursor=self.connection.cursor()
			pprint("connected to database")
		except:
			pprint("Cannot connect to database")
            
	def insertTTNGateway(self):
		postgres_insert_query = """ INSERT INTO public."SensorData" ("DeviceId","Level","Battery",app_id,dev_id,hardware_serial,
        port,counter,payload_raw,"time",frequency,modulation,data_rate,airtime,coding_rate,"TTNGatewayId",payload_fields)
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		record_to_insert = ("504","23","12","emrp2018","emrp2018dev01","08B5679A6D7G",1,7,"AKEO","2019-02-11",
        868,"LORA","SF7BW125",51456000,"4/5",380,str(payload_fields))
		self.cursor.execute(postgres_insert_query, record_to_insert)            

if __name__ == '__main__':
    Database_Connection=DatabaseConnection()
    r = .25 # growth rate / yr .25
    K = 100 # carrying capacity
    t = 40 # number of years
    num = np.zeros(t+1)

    num[0] = 1
    for i in range(t):
        num[i+1] = num[i]+r*num[i]*(1-num[i]/K)
        print(i,'insert',num[i])
        if i<=1:
            time.sleep(i)
            Database_Connection.insertTTNGateway() 
       
        else:
            time.sleep(num[i]-num[i-1])
            Database_Connection.insertTTNGateway() 
       

print(num)    
print('insert')
plt.plot(range(t+1),num, 'b')

plt.xlabel('Year')
plt.ylabel('Number')
plt.title('Growth rate: 0.25, Carrying Capacity = 100')
#plt.axvline(np.argmax(np.diff(num)),  color = 'k'  )
plt.show()