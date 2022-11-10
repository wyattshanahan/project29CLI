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
class User:
    def __init__(self, username):
        self.username = username

# class definitions and functions go above here

# Main menu/ driver code (write a better comment than this for the final version)
#each option below should launch the respective menu
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
    #fix formatting of exit
    # Else if 5 is entered, then launch the exit menu
    elif (selection == "5"):
        while (1):
            print("Do you wish to log out?")
            print("1. Log out")
            print("2. Go back")
            selection = input("Input a number to select a menu option: ")
            if (selection == "1"):
                print(" Logging you out")
                killprogram = True
                break
            elif (selection == "2"):
                break
            else:
                print("Invalid option, please try again")
    else:
        print("Invalid option, please try again")