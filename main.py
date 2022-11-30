# Imports libraries and dependencies
import mysql.connector
from mysql.connector import Error
import sys
from User import User
from Cart import Cart
from OrderHistory import OrderHistory
from functions import loginMenu, deleteUser, grabGame


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

# Main menu/ driver code (write a better comment than this for the final version)
# each option below should launch the respective menu

# Checks for valid password login
currUser = loginMenu(cursor, mydb)
if isinstance(currUser, User):
    killprogram = False
else:
    print("Logging you out and ending your session.\n")
    killprogram = True

# main driver code, launches after login or registration
while (killprogram == False):
    print("\nMain Menu:")
    print("1. Shop Inventory")
    print("2. View and Edit Cart")
    print("3. View and Edit User Information")
    print("4. View Order History")
    print("5. Log Out")
    selection = input("Input a number to select a menu option: ")

# Inventory submenu, allows a user to view inventory and add it to their cart
    if (selection == "1"):
        while True:
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
                GameIDs = tuple(GameIDs)
                for outer in GameIDs:
                    for inner in outer:
                        currGame = inner
                        query = ("SELECT Title FROM inventory WHERE GameID = %s")
                        cursor.execute(query, (currGame,))
                        titles = cursor.fetchall()
                        print(str(currGame) + ". " + str(titles[0][0]))
            elif(userInput == "2"):
                currGame = grabGame(cursor, mydb)
                if currGame == 'abort':
                    break
                else:
                    currGame.viewInfo()
            elif(userInput == "3"):
                currGame = grabGame(cursor,mydb)
                quan = int(input("How many copies of this would you like to purchase?"))
                quan = abs(quan)
                UID = currUser.userID
                userCart = Cart(currUser.userID,currGame.title,currGame.gameID,quan)
                userCart.insertCart(cursor,mydb)
                break
            elif(userInput == "4"):
                break
            else:
                print("Invalid option, please try again\n")

# Cart submenu, allows a user to view their cart, check out, and remove items from their cart
    elif (selection == "2"):
        userCart = Cart(currUser.userID)
        while True:
            print("Cart Menu:")
            print("1. View Cart")
            print("2. Check out")
            print("3. Remove an Item From Cart")
            print("4. Go Back")
            cart_selection = input("Input a number to select a menu option: ")
            # Calls the viewCart class function and returns back to the menu once done
            if (cart_selection == "1"):
                userCart.viewCart(cursor)
            # Calls the checkout class function and returns the the menu once done
            elif (cart_selection == "2"):
                userCart.checkout(cursor, mydb)
                print("Thank you for shopping with us!")
                break
            # Calls the removeCart class function and returns to the menu once done
            elif (cart_selection == "3"):
                output = userCart.removeCart(cursor, mydb)
                if (output == True):
                    print("Successfully removed!")
                break
            # Return to Main Menu
            elif (cart_selection == "4"):
                break
            else:
                print("Invalid option, please try again.")

# User information menu. Allows a user to view their account information, edit the information, or delete their account
    elif (selection == "3"):
        while True:
            print("User Information: ")
            print("1. View User Information")
            print("2. Edit User Information")
            print("3. Delete User Account")
            print("4. Go Back")
            userinfo_selection = input("Input a number to select a menu option: ")
            # Selection of 1 calls the viewInfo class function and then returns to the main menu
            if (userinfo_selection == '1'):
                currUser.viewInfo()
            # Selection of 2 calls the viewInfo class function, then the editUser function to let users edit information.
            # It then returns to the home menu
            elif (userinfo_selection == '2'):
                currUser.viewInfo()
                currUser.editUser(cursor,mydb)
                break
            # Selection of 3 calls the removeCart and deleteUser class function. If the user is deleted, then the session is ended
            # If the user is not deleted (out == False), then the user is returned to the main menu
            elif (userinfo_selection == '3'):
                cartID = currUser.userID
                out = deleteUser(currUser,cursor,mydb)
                if (out == True):
                    userCart = Cart(currUser.userID)
                    output = userCart.removeCart(cursor, mydb)
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
        userOrderHistory = OrderHistory(currUser.userID)
        while True:
            print("Order History Menu:")
            print("1. View Order History")
            print("2. Go Back")
            userInput = input("Input a number to select a menu option:")
            if (userInput == "1"):
                userOrderHistory.viewOrderHistory(cursor)
                break
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
# clean this menu up

# add comments/documentation
    #comments/doc for main
    #comments/doc for cart class
    #comments/doc for inventory class
    #comments/doc for history class
# clean up code
#   should this be pythonic? check rubric
#
