# Imports libraries and dependencies
from User import User
from VideoGame import VideoGame

# Function to create a new user. Returns a user object for the session and writes to the SQL Database
def makeNewUser(cursor, mydb):
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
def loginMenu(cursor, mydb):
    print("Welcome to Project29 CLI Game Store\n")
    print("Please select a menu option to continue: ")
    while (True):
        print("1. Login")
        print("2. Create a New Account")
        print("3. Exit")
        userInput = input("Input a number to select a menu option: ")
        if(userInput == "1"):
            currUser = login(cursor)
            return currUser
        elif(userInput == "2"):
            currUser = makeNewUser(cursor, mydb)
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
def login(cursor):
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

# shell function to facilitate password checks and deleting a user account
def deleteUser(currUser, cursor, mydb):
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

# function to build a VideoGame object, used for Cart class and inventory class submenus
def grabGame(cursor, mydb):
    while (True):
        currGameID = input("Enter a GameID: ")
        if (currGameID == 'abort'):
            return 'abort'
        query = ("SELECT * FROM inventory WHERE GameID = %s")
        cursor.execute(query, (currGameID,))
        result = cursor.fetchall()
        if (result == []):
            print("Invalid gameID. Please try again.")
        else:
            result = result[0]
            currGame = VideoGame(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            return currGame
