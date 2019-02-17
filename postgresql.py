import psycopg2
import time

connection = psycopg2.connect(user="emrp2018",
	                             password="emrp2018!",
	                             host="hsrw.space",
	                             port="5432",
	                             database="emrp2018")
# allows python code to execute psql
cur = connection.cursor()
sql = 'select \"Level",b.time from \"SensorData\" a left join \"TTNGateway\" b on a.\"TTNGatewayId\"=b.\"GatewayId\"'
cur.execute(sql)
# print(cur.fetchall())
data = cur.fetchall()
data
import pandas as pd
df = pd.DataFrame(data)
df.head(3)
df.columns=['level','time']
import matplotlib.pyplot as plt
plt.plot(df.time,df.level)
plt.xlabel('time')
plt.ylabel('level')
plt.title('level vs time')
plt.savefig('moers_01.png')  
plt.show()
cur.close()


#
# while(True):            # show all the data
# 	connection = psycopg2.connect(user="emrp2018",
# 	                             password="emrp2018!",
# 	                             host="hsrw.space",
# 	                             port="5432",
# 	                             database="emrp2018")
# 	# allows python code to execute psql
# 	cur = connection.cursor()
# 	sql = 'select \"Level",b.time from \"SensorData\" a left join \"TTNGateway\" b on a.\"TTNGatewayId\"=b.\"GatewayId\"'
# 	cur.execute(sql)
# 	# print(cur.fetchall())
# 	data = cur.fetchall()
# 	data
# 	import pandas as pd          
# 	df = pd.DataFrame(data)        
# 	df.head(3)                      # load index level time
# 	df.columns=['level','time']
# 	import matplotlib.pyplot as plt
# 	plt.plot(df.time,df.level)
# 	plt.xlabel('time')
# 	plt.ylabel('level')
# 	plt.title('level vs time')
# 	plt.show()
# 	cur.close()
# 	#wait 2 hours, renew  data
# 	time.sleep(2*3600)

