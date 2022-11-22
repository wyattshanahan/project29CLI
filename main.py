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

# Function to create a new user. Returns a user object for the session and writes to the SQL Database
def makeNewUser():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    while (1):
        email = input("Enter your email address: ")
        query = ("SELECT email FROM Users WHERE email = %s")
        cursor.execute(query, (email,))
        status = cursor.fetchall()
        if status != []:
            print("Email address is already registered. Please try again")
        else:
            break
    telephone = input("Enter your telephone number: ")
    while(1):
        username = input("Enter your desired username: ")
        query = ("SELECT username FROM Users WHERE username = %s")
        cursor.execute(query,(username,))
        status = cursor.fetchall()
        if status != []:
            print("Username already exists. Please try again")
        else:
            break
    password = input("Enter your desired password: ")
    street = input("Enter your street address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    userZip = input("Enter your zip/postal code: ")
    cardNum = input("Enter your credit card number: ")
    cardDate = input("Enter your card's expiration date: ")
    cardName = input("Enter the name on your card: ")
    cardCVV = input("Enter the security code on your card: ")
    query = ("SELECT COUNT(1) FROM Users")
    cursor.execute(query,)
    userID = cursor.fetchall()
    userID = userID[0]
    userID = userID[0]
    int(userID)
    userID +=1
    newUser = User(userID, fname, lname, street, city, state, userZip, username, password, email, telephone, cardNum, cardCVV, cardName , cardDate, orderNum = 0)
    newUser.makeDB(cursor, mydb)
    return newUser

# Function to create a user object for the session for an existing user
def makeCurrUser(result):
    result = result[0]
    currUser = User(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15])
    return currUser

# Function for the login menu, returns currUser object
def loginMenu():
    print("Welcome to Project29 CLI Game Store\n")
    print("Please select a menu option to continue: ")
    while userInput not in ['1', '2', '3']:
        print("1. Login")
        print("2. Create a New Account")
        print("3. Exit")
        userInput = input("Please enter an integer menu option: ")
        if(userInput == "1"):
            currUser = login()
            return currUser
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


# Function to log in an existing user. Returns currUser to loginMenu()
def login():
    print("Login to an existing account")
    while (1):
        userInput = ("Enter your username. Type 'abort' to exit this process. ")
        query = ("SELECT password FROM Users WHERE username = %s")
        cursor.execute(query, (userInput,))
        username = cursor.fetchall()
        if (username[0] == userInput):
            username = username[1]
            break
        elif (userInput == 'abort'):
            return 1
        else:
            print("Invalid username. Please try again.")
    query = ("SELECT * FROM Users WHERE username=%s")
    cursor.execute(query, (username,))
    currUser = cursor.fetchall()
    return makeCurrUser(currUser)

# Main menu/ driver code (write a better comment than this for the final version)
#each option below should launch the respective menu
currUser = loginMenu()
killprogram = False
while (killprogram == False):
    print("\nMain Menu:")
    selection = ""
    while selection not in ['1', '2', '3', '4', '5']:
        print("1. Shop Inventory")
        print("2. View and Edit Cart")
        print("3. View and Edit User Information")
        print("4. View Order History")
        print("5. Log Out")
        selection = input("Input a number to select a menu option: ")
        if (selection == "1"):
            print("this will eventually show inventory")
            #login()
            makeNewUser()
        elif (selection == "2"):
            print("this will eventually show the cart menu")
        elif (selection == "3"):
            # userinfo_selection variable so that the while loop works
            userinfo_selection = ''
            while userinfo_selection not in ['1', '2', '3', '4']:
                print("User Information: ")
                print("1. View User Information")
                print("2. Edit User Information")
                print("3. Delete User Account")
                print("4. Go Back")
                selection = input("Input a number to select a menu option: ")
                if (userinfo_selection == "1"):
                    print("display User Information here with a function")
                elif (userinfo_selection == "2"):
                    print("edit user info menu, after displaying info")
                elif (userinfo_selection == "3"):
                    print("Delete account menu, used to confirm deletion then function to delete it")
                elif (userinfo_selection == "4"):
                    break
                else:
                    print("Invalid option, please try again\n")
        elif (selection == "4"):
            print("this will eventually show order history")
        # fix formatting of exit
        # Else if 5 is entered, then launch the exit menu
        elif (selection == "5"):
            while selection not in ['1', '2']:
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
            print("Invalid option, please try again\n")


#TO-DO:
# login function
# finish login menu
# finish exit loop for login menu
# main menu
# user class grabber from DB (part of login)
#functions to grab from SQL to build user, setters including writing to the DB
