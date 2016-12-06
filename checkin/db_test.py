#this is where the clients ID numbers will be stored and searched for validity later
#!/usr/bin/python
import MySQLdb

#open database connection
db = MySQLdb.connect("localhost","root","gits2501","CLIENTS")
#prepare a cursor object using cursor() method
cursor = db.cursor()
#execute SQL query using execute() method
cursor.execute("DROP TABLE IF EXISTS CLIENTS")
#fetch a single row using fetchone() method
#data = cursor.fetchone() - this is from the old module that just connects to the database
#print "Database version is: %s" % data

#make a table
client_table = """CREATE TABLE CLIENTS(
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20) NOT NULL,
ID INT NOT NULL,
PRIMARY KEY(ID)) """

cursor.execute(client_table)
#disconnect from server
db.close()

#note: possibly put this code into a function and allow /views/ to pass the user's input onto the function as an arg
#the function will then add the arg to the database