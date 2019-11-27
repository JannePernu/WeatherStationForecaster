import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def DataRetreiver(wtData):
	try:
		print('Retreiving Data')
		connection = mysql.connector.connect(host='87.92.64.6',
											 database='projekti',
											 user='projekti',
											 password='Saaasema')

		mySql_insert_query = """SELECT * FROM Historical"""
		cursor = connection.cursor()
		cursor.execute(mySql_insert_query)
		records = cursor.fetchall()
		
		for row in records:
			#print(row)
			wtData[0].append(row[3])
			wtData[1].append(row[4])
			wtData[2].append(row[5])
			wtData[3].append(row[1])
		return wtData

	except mysql.connector.Error as error:
		print("Failed to retreive record ".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			cursor.close()
			print('Data Retreived')
			print("MySQL connection is closed")
			
			
def DataSender(data):
	try:
		connection = mysql.connector.connect(host='87.92.64.6',
									 database='projekti',
									 user='projekti',
									 password='Saaasema')

		for row in data:
			mySql_insert_query = """INSERT INTO Historical  
								   (Date, Time, TempH, AirPH, HumidH) 
								   VALUES (%s, %s, %s, %s, %s) """
			records_to_insert = [(row[0], row[1], 
								  row[2], row[3], row[4])]

			cursor = connection.cursor()
			cursor.executemany(mySql_insert_query, records_to_insert)
			connection.commit()

	except mysql.connector.Error as error:
		print("Failed to insert record to table {}".format(error))

	finally:
		if (connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")
