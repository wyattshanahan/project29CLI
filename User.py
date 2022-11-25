# User class file containing the constructor, getters, setters, deletion, makeDB, and password checker functions.
class User:
    def __init__(self, userID, fname, lname, street, city, state, userZip, username, password, email, telephone, cardNum, cvv, cardName, cardDate, orderNum):
        self.userID = userID
        self.fname = fname
        self.lname = lname
        self.street = street
        self.city = city
        self.state = state
        self.zip = userZip
        self.username = username
        self.password = password
        self.email = email
        self.telephone = telephone
        self.cardNum = cardNum
        self.cvv = cvv
        self.cardName = cardName
        self.cardDate = cardDate
        self.orderNum = orderNum
    def makeDB(self, cursor, mydb):
        cursor = cursor
        query = "INSERT INTO Users (userID, fname, lname, street, city, state, userZip, username, password, email, telephone, cardNum, cvv, cardName,cardDate, orderNum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (self.userID, self.fname, self.lname, self.street, self.city, self.state, self.zip, self.username, self.password, self.email, self.telephone, self.cardNum, self.cvv, self.cardName, self.cardDate, self.orderNum)
        cursor.execute(query, data)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")
        print()
    def getID(self):
        return self.userID
    def getfname(self):
        return self.fname
    def getlname(self):
        return self.lname
    def getstreet(self):
        return self.street
    def getcity(self):
        return self.city
    def getstate(self):
        return self.state
    def getzip(self):
        return self.zip
    def getusername(self):
        return self.username

   #do we need a getter for password?
    def getpassword(self):
        return self.password
    def getemail(self):
        return self.email
    def gettelephone(self):
        return self.telephone
    def getcardnum(self):
        return self.cardNum
    def getcvv(self):
        return self.cvv
    def getcardname(self):
        return self.cardName
    def getcarddate(self):
        return self.cardDate
    def getordernum(self):
        return self.orderNum

    def setfname(self, cursor, mydb):
        self.fname = input("Enter a new first name: ")
        cursor = cursor
        query = ("UPDATE Users SET fname= %s WHERE userID = %s")
        cursor.execute(query, (self.fname, self.userID,))
        mydb.commit()
    def setlname(self, cursor, mydb):
        self.lname = input("Enter a new last name: ")
        cursor = cursor
        query = ("UPDATE Users SET lname=%s WHERE userID =%s")
        cursor.execute(query, (self.lname, self.userID,))
        mydb.commit()
    def setstreet(self, cursor, mydb):
        self.street = input("Enter a new street address: ")
        cursor = cursor
        query = ("UPDATE Users SET street=%s WHERE userID =%s")
        cursor.execute(query, (self.street, self.userID,))
        mydb.commit()
    def setcity(self, cursor, mydb):
        self.city = input("Enter a new city name: ")
        cursor = cursor
        query = ("UPDATE Users SET city=%s WHERE userID =%s")
        cursor.execute(query, (self.city, self.userID,))
        mydb.commit()
    def setstate(self, cursor, mydb):
        self.state = input("Enter a new state abbreviation: ")
        cursor = cursor
        query = ("UPDATE Users SET state=%s WHERE userID =%s")
        cursor.execute(query, (self.state, self.userID,))
        mydb.commit()
    def setzip(self, cursor, mydb):
        self.zip = input("Enter a new zip/postal code: ")
        cursor = cursor
        query = ("UPDATE Users SET userZip=%s WHERE userID =%s")
        cursor.execute(query, (self.zip, self.userID,))
        mydb.commit()
    def setusername(self, cursor, mydb):
        cursor = cursor
        while (True):
            username = input("Enter a new username: ")
            query = ("SELECT username FROM Users WHERE username = %s")
            cursor.execute(query, (username,))
            status = cursor.fetchall()
            if status != []:
                print("Username already exists. Please try again")
            else:
                break
        self.username = username
        query = ("UPDATE Users SET username=%s WHERE userID =%s")
        cursor.execute(query, (self.username, self.userID,))
        mydb.commit()
    def setpassword(self, cursor, mydb):
        good_password = False
        good_password = self.checkPassword(cursor)
        if (good_password == 'abort'):
            print("Action aborted.\n")
            return False
        elif (good_password == False):
            print ("Password check failed. Please try again")
            return False
        self.password = input("Enter your new password: ")
        cursor = cursor
        query = ("UPDATE Users SET password=%s WHERE userID =%s")
        cursor.execute(query, (self.password, self.userID,))
        mydb.commit()
    def setemail(self, cursor, mydb):
        cursor = cursor
        while (True):
            email = input("Enter a new email: ")
            query = ("SELECT email FROM Users WHERE userID = %s")
            cursor.execute(query, (email,))
            status = cursor.fetchall()
            if status != []:
                print("Email already exists. Please try again")
            else:
                break
        self.email = email
        query = ("UPDATE Users SET email=%s WHERE userID =%s")
        cursor.execute(query, (self.email, self.userID,))
        mydb.commit()
    def settelephone(self, cursor, mydb):
        self.telephone = input("Enter a new telephone number: ")
        cursor = cursor
        query = ("UPDATE Users SET telephone=%s WHERE userID =%s")
        cursor.execute(query, (self.telephone, self.userID,))
        mydb.commit()
    def setcardnum(self, cursor, mydb):
        self.cardNum = input("Enter a new card number: ")
        cursor = cursor
        query = ("UPDATE Users SET cardNum=%s WHERE userID =%s")
        cursor.execute(query, (self.cardNum, self.userID,))
        mydb.commit()
    def setcvv(self, cursor, mydb):
        self.cvv = input("Enter a new CVV number: ")
        cursor = cursor
        query = ("UPDATE Users SET cvv=%s WHERE userID =%s")
        cursor.execute(query, (self.cvv, self.userID,))
        mydb.commit()
    def setcardname(self, cursor, mydb):
        self.cardName = input("Enter a new card name: ")
        cursor = cursor
        query = ("UPDATE Users SET cardName=%s WHERE userID =%s")
        cursor.execute(query, (self.cardName, self.userID,))
        mydb.commit()
    def setcarddate(self, cursor, mydb):
        self.cardDate = input("Enter a new card expiration date: ")
        cursor = cursor
        query = ("UPDATE Users SET cardDate=%s WHERE userID =%s")
        cursor.execute(query, (self.cardDate, self.userID,))
        mydb.commit()
    def delete(self, cursor, mydb):
        continuer = self.checkPassword(cursor)
        if (continuer == 'abort'):
            print("Action aborted. \n")
            return False
        elif (continuer):
            while (True):
                userInput = input("Do you wish to delete your account? (y/n): ")
                if ((userInput == "y") or (userInput == "Y")):
                    print("Deleting your account from the system.")
                    cursor = cursor
                    query = "DELETE FROM Users WHERE userID=?"
                    cursor.execute(query, self.userID)
                    mydb.commit()
                    print(cursor.rowcount, "Account deleted successfully.")
                    print()
                    return True
                elif ((userInput == "n") or (userInput == "N")):
                    print("Aborting deletion.")
                    return False
                else:
                    print("Invalid input, please try again.\n")
        else:
            print("Incorrect password. Please try again")
    def checkPassword(self,cursor):
        while (True):
            userInput = input("Enter your password. Type 'abort' to exit this process. ")
            if (userInput == 'abort'):
                return 'abort'
            query = ("SELECT password FROM Users WHERE username = %s")
            cursor.execute(query, (self.username,))
            correctPassword = cursor.fetchall()
            correctPassword = correctPassword[0]
            if(correctPassword[0] == userInput):
                return True
            elif(userInput == 'abort'):
                return 'abort'
            else:
                print("Invalid password. Please try again.")

    def viewInfo(self):
        print("User Account Information\n")
        print("Name: " + self.fname + " " + self.lname)
        print("Address: " + self.street + " " + self.city + ", " + self.state + " " + self.zip)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Telephone: " + self.telephone)
        print("Payment Method: \n\tCard Number: " + str(self.cardNum) + "\n\tCVV: " + str(self.cvv) + "\n\tName on Card: " + self.cardName + "\n\tCard Expiration Date: " + self.cardDate)
        print("Number of Orders: " + str(self.orderNum))

    def editUser(self,cursor,mydb):
        exit = False
        while(exit == False):
            print("Select which value you wish to edit")
            print("1. First name")
            print("2. Last name")
            print("3. Street and Address")
            print("4. City")
            print("5. State")
            print("6. Zip/Postal Code")
            print("7. Username")
            print("8. Password")
            print("9. E-mail")
            print("10. Telephone")
            print("11. Card number")
            print("12. Card CVV")
            print("13. Name on Card")
            print("14. Card Expiration Date")
            print("15. Exit")
            userInput = input("Input a number to select a menu option: ")
            if (userInput == "1"):
               self.setfname(cursor, mydb)
            elif (userInput == "2"):
                self.setlname(cursor, mydb)
            elif(userInput == "3"):
                self.setstreet(cursor, mydb)
            elif (userInput == "4"):
                self.setcity(cursor, mydb)
            elif (userInput == "5"):
                self.setstate(cursor, mydb)
            elif (userInput == "6"):
                self.setzip(cursor, mydb)
            elif (userInput == "7"):
                self.setusername(cursor, mydb)
            elif (userInput == "8"):
                self.setpassword(cursor,mydb)
            elif (userInput == "9"):
                self.setemail(cursor, mydb)
            elif (userInput == "10"):
                self.settelephone(cursor, mydb)
            elif (userInput == "11"):
                self.setcardnum(cursor, mydb)
            elif (userInput == "12"):
                self.setcvv(cursor, mydb)
            elif (userInput == "13"):
                self.setcardname(cursor, mydb)
            elif (userInput == "14"):
                self.setcarddate(cursor, mydb)
            elif (userInput == "15"):
                break
            else:
                print("Invalid input, please try again.")