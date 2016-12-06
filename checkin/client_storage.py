#this will be a test file I will use to update the mySQL data base
import MySQLdb
import mysql.connector
from mysql.connector.errors import Error

#Use a function to insert new information into the database

def insert(info):
	#open a connection
	db = MySQLdb.connect('localhost','root','gits2501', 'CLIENTS')
	#prepare a cursor
	cursor = db.cursor()
	#prepare SQL query
	sql = "INSERT INTO clients(ID) VALUES (%s)" % info

	try:
		#execute the command
		cursor.execute(sql)
		#commit changes to the database
		db.commit()
	except mysql.connector.Error as e:
		#display the error message MySQL returns to the user
		return e
		

	#disconnect from server
	db.close()
