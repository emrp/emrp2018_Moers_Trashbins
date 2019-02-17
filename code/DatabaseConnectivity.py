import psycopg2
from pprint import pprint

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection= psycopg2.connect(
			"dbname='' user='' host='' password=''")
			self.connection.autocommit=True
			self.cursor=self.connection.cursor()
			pprint("connected to database")
		except:
			pprint("Cannot connect to database")
	def insertTTNGateway(self):
		postgres_insert_query = """ INSERT INTO public."TTNGateway" (gtw_id,timestamp,channel,rssi,snr,longitude,latitude,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING "GatewayId" """
		record_to_insert = ("eui-b2345jk",78373778,"2","-78","6","6.5485168","51.3527789","2011-11-05")



		#pprint(postgres_insert_query)
		self.cursor.execute(postgres_insert_query, record_to_insert)
		returnValue = self.cursor.fetchone()[0]	
		pprint(returnValue)
if __name__ == '__main__':
	Database_Connection=DatabaseConnection()
	Database_Connection.insertTTNGateway()		

