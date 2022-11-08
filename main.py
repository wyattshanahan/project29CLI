import mysql.connector;
import sys;
# Attempts a connection to the database server, displays a message if a connection is successful
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "project29"
    )
    print("Successfully connected to the database")
# If connecting to the database server, an error message is displayed and the process ends
except:
    print("Failed to connect to the database")
    sys.exit()
print("code executed and connected successfully")

# Class definition for the user class. This class still needs to be written
class user:
    def __init__(self, username):
        self.username = username
