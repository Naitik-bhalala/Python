import mysql.connector
db_connection = mysql.connector.connect(
  host= "localhost",
  user= "root",
  passwd= ""
  )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE test")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)






#import mysql.connector
#Name = 'naitik'
#Email = 'abc'
#Password = 1234
#Gender = 'male'
#db_connection = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  passwd="",
#  database="test"
#  )
#db_cursor = db_connection.cursor()
#signup_sql_query = "INSERT INTO signup(name, email, password, gender) VALUES('Name','Email','Password','Gender')"


#db_cursor.execute(signup_sql_query)

#db_connection.commit()
#print(db_cursor.rowcount, "Record Inserted")