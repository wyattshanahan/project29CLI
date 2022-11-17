import mysql.connector
import sys
from User import User
# Attempts a connection to the database server, displays a message if a connection is successful
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project29"
    )
    print("Successfully connected to the database")
# If connecting to the database server fails, an error message is displayed and the process ends
except:
    print("Failed to connect to the database")
    sys.exit()

cursor = mydb.cursor()

def makeNewUser():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    #SQL to check for existing already
    email = input("Enter your email: ")
    telephone = input("Enter your telephone number: ")
    #SQL to check for it already existing
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")
    street = input("Enter your street address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    userZip = input("Enter your zip/postal code: ")
    cardNum = input("Enter your credit card number: ")
    cardDate = input("Enter your card's expiration date: ")
    cardName = input("Enter the name on your card: ")
    cardCVV = input("Enter the security code on your card: ")
    userID = "some sql command to get number of rows in a table +1"
    newUser = User(userID, fname, lname, street, city, state, userZip, username, password, email, telephone, cardNum, cardCVV, cardName , cardDate, orderNum = 0)
    newUser.makeDB(cursor, mydb)
    return(newUser)

def makeCurrUser():
    print("this will query with the username, separate the SQL output, and create a user object with the information")
    # class needs a function to construct a user based on data received from an SQL query. Utilize the user class constructor for doing this
def loginMenu():
    print("Welcome to Project29 CLI Game Store\n")
    while userInput not in ['1', '2', '3']:
        print("Please select a menu option to continue: ")
        print("1. Login")
        print("2. Create a New Account")
        print("3. Exit")
        userInput = input("Please enter an integer menu option: ")
        if(userInput == "1"):
            print("run the login function")
            #currUser = login()
            #return currUser
        elif(userInput == "2"):
            currUser = makeNewUser()
            return currUser
        elif(userInput == "3"):
            userInput = input("Do you wish to exit? (y/n)")
            while userInput not in ['y', 'n']:
                if (userInput == "y" or "Y"):
                    print("exit")
                elif(userInput == "n" or "N"):
                    print("dont exit")
                else:
                    print("Invalid input, please try again.\n")
        else:
            print("Invalid input, please try again.\n")

#function for login process
def login():
    print("Login to an existing account")
    username = input("Please enter your username: ")
    cursor.execute("SELECT userID FROM Users WHERE username=?", username)
    userID = cursor.fetchall()


#function to create a user object in python during session (iterates a tuple from the DB)
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
        makeNewUser()
    elif (selection == "2"):
        print("this will eventually show the cart menu")
    elif (selection == "3"):
        while (1):
            print("User Information: ")
            print("1. View User Information")
            print("2. Edit User Information")
            print("3. Delete User Account")
            print("4. Go Back")
            selection = input("Input a number to select a menu option: ")
            if (selection == "1"):
                print("display User Information here with a function")
            elif (selection == "2"):
                print("edit user info menu, after displaying info")
            elif (selection == "3"):
                print("Delete account menu, used to confirm deletion then function to delete it")
            elif (selection == "4"):
                break
            else:
                print("Invalid option, please try again")
    elif (selection == "4"):
        print("this will eventually show order history")
    # fix formatting of exit
    # Else if 5 is entered, then launch the exit menu
    elif (selection == "5"):
        while (1):
            print("\nDo you wish to log out?")
            print("1. Log Out")
            print("2. Go Back")
            selection = input("Input a number to select a menu option: ")
            if selection == "1":
                print("\nYou will now be logged out")
                killprogram = True
                break
            elif (selection == "2"):
                break
            else:
                print("Invalid option, please try again")
    else:
        print("Invalid option, please try again")


#TO-DO:
# login function
# finish login menu
# finish exit loop for login menu
# main menu
# user class setters
# user class grabber from DB (part of login)
# SQL add support for when data item not found
#functions to grab from SQL to build user, setters including writing to the DB
