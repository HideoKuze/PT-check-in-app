#this will be a test file I will use to update the mySQL data base
import MySQLdb
import mysql.connector
from mysql.connector import errorcode
from django.contrib import messages

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
		print 'success'
		db.commit()
	except MySQLdb.Error as e:
		#return the first element in the tuple that contains the error message, which will be a the errorcode
		 if e[0] == 1062:
		 	return e[0]
		 if e[0] == 1054:
		 	return e[0]

	#disconnect from server
	db.close()

insert('2503')