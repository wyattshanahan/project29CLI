import mysql.connector
import sys
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

# class definitions and functions go above here

# Main menu/ driver code (write a better comment than this for the final version)
killprogram = False
while (killprogram == False):
    print("\nMain Menu:")
    print("1. Shop Inventory")
    print("2. View and Edit Cart")
    print("3. View and Edit User Information")
    print("4. View Order History")
    print("5. Log Out")
    selection = input("Input a number to select a menu option: ")
    if (selection == "1"):
        print("this will eventually show inventory")
    elif (selection == "2"):
        print("this will eventually show the cart menu")
    elif (selection == "3"):
        print("this will eventually show the user info menu")
    elif (selection == "4"):
        print("this will eventually show order history")
    elif (selection == "5"):
        print("Exiting the program")
        killprogram = True
    else:
        print("Invalid option, please try again")