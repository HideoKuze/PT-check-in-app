import mysql.connector
from mysqldb.connector import errorcode


cnx = mysqldb.connect('localhost', 'root', 'gits2501', 'CLIENTS')
cursor = cnx.cursor()
try:
  cursor.execute("DROP TABLE spam")
except mysqldb.connector.Error as err:
  if err.errno == errorcode.ER_BAD_TABLE_ERROR:
    print("Creating table spam")
  else:
    raise