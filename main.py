# Imports libraries and dependencies
import mysql.connector
from mysql.connector import Error
import sys
from User import User
from VideoGame import VideoGame
# from Cart import Cart
# from OrderHistory import OrderHistory


# Attempts a connection to the database server, displays a message if a connection is successful
try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="project29"
    )
    print("Successfully connected to the database")
# Returns a specific error code if possible if the connection fails
except Error as e:
    print("Error connecting to the database: ", e)
    sys.exit()
# If connecting to the database server fails, an error message is displayed and the process ends
except:
    print("Failed to connect to the database")
    sys.exit()

cursor = mydb.cursor()

# Function to create a new user. Returns a user object for the session and writes to the SQL Database
def makeNewUser():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    while(True):
        email = input("Enter your email address: ")
        query = ("SELECT email FROM Users WHERE email = %s")
        cursor.execute(query, (email,))
        status = cursor.fetchall()
        if status != []:
            print("Email address is already registered. Please try again")
        else:
            break
    telephone = input("Enter your telephone number: ")
    while(True):
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
    while (True):
        print("1. Login")
        print("2. Create a New Account")
        print("3. Exit")
        userInput = input("Input a number to select a menu option: ")
        if(userInput == "1"):
            currUser = login()
            return currUser
        elif(userInput == "2"):
            currUser = makeNewUser()
            return currUser
        elif(userInput == "3"):
            while (True):
                userInput = input("Do you wish to exit? (y/n): ")
                if ((userInput == "y") or (userInput == "Y")):
                    return False
                elif((userInput == "n") or (userInput == "N")):
                    break
                else: print("Invalid input, please try again.\n")
        else:
            print("Invalid input, please try again.\n")

# Function to log in an existing user. Returns currUser to loginMenu()
def login():
    print("\nLog into an existing account.")
    while (True):
        userInput = input("Enter your username. Type 'abort' to exit this process. ")
        if (userInput == 'abort'):
            return 1
        query = ("SELECT username FROM Users WHERE username = %s")
        cursor.execute(query, (userInput,))
        username = cursor.fetchall()
        if (username == []):
            print("Invalid username. Please try again.")
        else:
            username = username[0]
            if(username[0] == userInput):
                username = username[0]
                break
    query = ("SELECT * FROM Users WHERE username = %s")
    cursor.execute(query, (username,))
    currUser = cursor.fetchall()
    currUser =  makeCurrUser(currUser)
    loginGood = currUser.checkPassword(cursor)
    if (loginGood == True):
        return currUser

def deleteUser(user,cursor, mydb):
    continuer = currUser.checkPassword(cursor)
    if (continuer == 'abort'):
        print("Action aborted. \n")
        return False
    elif (continuer):
        while (True):
            userInput = input("Do you wish to delete your account? (y/n): ")
            if ((userInput == "y") or (userInput == "Y")):
                print("Deleting your account from the system.")
                out = currUser.delete(cursor, mydb)
                return out
            elif ((userInput == "n") or (userInput == "N")):
                print("Aborting deletion.")
                return False
            else:
                print("Invalid input, please try again.\n")
    else:
        print("Incorrect password. Please try again")

# Main menu/ driver code (write a better comment than this for the final version)
# each option below should launch the respective menu

# Checks for valid password login
currUser = loginMenu()
if isinstance(currUser, User):
    killprogram = False
else:
    print("Logging you out and ending your session.\n")
    killprogram = True

# main driver code, launches after login or registration
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

    # Inventory submenu, allows a user to view inventory and add it to their cart
        if (selection == "1"):
            userInput = ''
            while userInput not in ['1', '2', '3']:
                print("\nInventory menu: ")
                print("1. View Inventory")
                print("2. View a Specific Item")
                print("3. Add Item to Cart")
                print("4. Go Back")
                userInput = input("Input a number to select a menu option: ")
                if(userInput == "1"):
                    print("\nInventory: ")
                    cursor.execute("SELECT GameID FROM inventory")
                    GameIDs = cursor.fetchall()
                    GameIDs = GameIDs[0]
                    cursor.execute("SELECT Title FROM inventory")
                    titles = cursor.fetchall()
                    titles = titles[0]
                    for i in range(0,len(titles)):
                        print(str(GameIDs[i]) + ". " + str(titles[i]))
                elif(userInput == "2"):
                    while (True):
                        userInput = input("\nEnter 'abort' to exit this menu.\nEnter a GameID (listed before a game title) to view it's details:")
                        if (userInput == 'abort'):
                            break
                        query = ("SELECT * FROM inventory WHERE GameID = %s")
                        cursor.execute(query, (userInput,))
                        result = cursor.fetchall()
                        if (result == []):
                            print("Invalid username. Please try again.")
                        else:
                            result = result[0]
                            if (result[0] == userInput):
                                result = result[0]
                                currGame = VideoGame(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
                                currGame.viewInfo()
                                break
                elif(userInput == "3"):
                    print("Add a game to cart by gameid")
                elif(userInput == "4"):
                    break
                else:
                    print("Invalid option, please try again\n")

    # Cart submenu, allows a user to view their cart, check out, and remove items from their cart
        elif (selection == "2"):
            cart_selection = ''
            while cart_selection not in ['1', '2', '3', '4']:
                print("Cart Menu:")
                print("1. View Cart")
                print("2. Check out")
                print("3. Remove an Item From Cart")
                print("4. Go Back")
                cart_selection = input("Input a number to select a menu option: ")
                if (cart_selection == "1"):
                    print("view cart")
                elif (cart_selection == "2"):
                    print("check out")
                elif (cart_selection == "3"):
                    print("Remove from cart")
                elif (cart_selection == "4"):
                    break
                else:
                    print("Invalid option, please try again.")

    # User information menu. Allows a user to view their account information, edit the information, or delete their account
        elif (selection == "3"):
            # userinfo_selection variable so that the while loop works
            userinfo_selection = ''
            while userinfo_selection not in ['1', '2', '3', '4']:
                print("User Information: ")
                print("1. View User Information")
                print("2. Edit User Information")
                print("3. Delete User Account")
                print("4. Go Back")
                userinfo_selection = input("Input a number to select a menu option: ")
                # Selection of 1 calls the viewInfo class function and then returns to the main menu
                if (userinfo_selection == '1'):
                    currUser.viewInfo()
                    break
                # Selection of 2 calls the viewInfo class function, then the editUser function to let users edit information.
                # It then returns to the home menu
                elif (userinfo_selection == '2'):
                    currUser.viewInfo()
                    currUser.editUser(cursor,mydb)
                    break
                # Selection of 3 calls the deleteUser class function. If the user is deleted, then the session is ended
                # If the user is not deleted (out == False), then the user is returned to the main menu
                elif (userinfo_selection == '3'):
                    out = deleteUser(currUser,cursor,mydb)
                    if (out == True):
                        killprogram = True
                        break
                    elif (out == False):
                        break
                    else:
                        # This code should never be hit, if it is then it will return users to main menu.
                        print("An unexpected error occurred. Please contact the site administrators.\n")
                        break
                # Selection of 4 returns the User to the main menu
                elif (userinfo_selection == "4"):
                    break
                # If no valid input is received, an error message is displayed and the menu loops
                else:
                    print("Invalid option, please try again\n")

        elif (selection == "4"):
            print("Order History:")
            print("1. View Order History")
            print("2. Go Back")
            userInput = input("Input a number to select a menu option:")
            if (userInput == "1"):
                print("view order history")
            elif (userInput == "2"):
                break
            else:
                print("Invalid option, please try again")
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
                    print("Invalid input, please try again.\n")
        else:
            print("Invalid input, please try again.\n")


#TO-DO:
# main menu
# sub menus
# decrement stock upon purchase
# write out the purchase program
# password length

# view cart option
# checkout function
# remove item from cart
# go back option for cart

# view order history
# go back from order history

# inventory menu
# view inventory
# to make this work, use a loop to create game options, numbered, and display info about them
# add item to cart

# add comments/documentation
    #comments/doc for main
    #comments/doc for cart class
    #comments/doc for inventory class
    #comments/doc for history class
# clean up code
#   should this be pythonic? check rubric
#
