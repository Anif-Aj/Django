import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123'
)

#prepare cursor object
cursorObject =database.cursor()


# create a database
cursorObject.execute("CREATE DATABASE anifcompany")
print("All Done!")