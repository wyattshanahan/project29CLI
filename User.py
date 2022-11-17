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

    def setfname(self, new_fname, cursor, mydb):
        self.fname = new_fname
        cursor = cursor
        query = ("UPDATE Users SET fname= %s WHERE userID = %s")
        cursor.execute(query, (new_fname, self.userID,))
        mydb.commit()
    def setlname(self, new_lname, cursor, mydb):
        self.lname = new_lname
        cursor = cursor
        query = ("UPDATE Users SET lname=%s WHERE userID =%s")
        cursor.execute(query, (new_lname, self.userID,))
        mydb.commit()
    def setstreet(self, new_street, cursor, mydb):
        self.street = new_street
        cursor = cursor
        query = ("UPDATE Users SET street=%s WHERE userID =%s")
        cursor.execute(query, (new_street, self.userID,))
        mydb.commit()
    def setcity(self, new_city, cursor, mydb):
        self.city = new_city
        cursor = cursor
        query = ("UPDATE Users SET city=%s WHERE userID =%s")
        cursor.execute(query, (new_city, self.userID,))
        mydb.commit()
    def setstate(self, new_state, cursor, mydb):
        self.state = new_state
        cursor = cursor
        query = ("UPDATE Users SET state=%s WHERE userID =%s")
        cursor.execute(query, (new_state, self.userID,))
        mydb.commit()
    def setzip(self, new_zip, cursor, mydb):
        self.zip = new_zip
        cursor = cursor
        query = ("UPDATE Users SET userZip=%s WHERE userID =%s")
        cursor.execute(query, (new_zip, self.userID,))
        mydb.commit()
    def setusername(self, new_name, cursor, mydb):
        self.username = new_name
        cursor = cursor
        query = ("UPDATE Users SET username=%s WHERE userID =%s")
        cursor.execute(query, (new_name, self.userID,))
        mydb.commit()
    def setpassword(self, new_password, cursor, mydb):
        good_password = False
        while(good_password != True):
            userInput = input("Please enter your password to continue. To exit, please type 'abort'.")
            if (userInput == "abort"):
                return 1
            good_password = self.checkPassword(self,userInput,self.userID)
        self.password = new_password
        cursor = cursor
        query = ("UPDATE Users SET password=%s WHERE userID =%s")
        cursor.execute(query, (new_password, self.userID,))
        mydb.commit()
    def setemail(self, new_email, cursor, mydb):
        self.email = new_email
        cursor = cursor
        query = ("UPDATE Users SET email=%s WHERE userID =%s")
        cursor.execute(query, (new_email, self.userID,))
        mydb.commit()
    def settelephone(self, new_phone, cursor, mydb):
        self.telephone = new_phone
        cursor = cursor
        query = ("UPDATE Users SET telephone=%s WHERE userID =%s")
        cursor.execute(query, (new_phone, self.userID,))
        mydb.commit()
    def setcardnum(self, new_cardnum, cursor, mydb):
        self.cardNum = new_cardnum
        cursor = cursor
        query = ("UPDATE Users SET cardNum=%s WHERE userID =%s")
        cursor.execute(query, (new_cardnum, self.userID,))
        mydb.commit()
    def setcvv(self, new_cvv, cursor, mydb):
        self.cvv = new_cvv
        cursor = cursor
        query = ("UPDATE Users SET cvv=%s WHERE userID =%s")
        cursor.execute(query, (new_cvv, self.userID,))
        mydb.commit()
    def setcardname(self, new_cardname, cursor, mydb):
        self.cardName = new_cardname
        cursor = cursor
        query = ("UPDATE Users SET cardName=%s WHERE userID =%s")
        cursor.execute(query, (new_cardname, self.userID,))
        mydb.commit()
    def setcarddate(self, new_carddate, cursor, mydb):
        self.cardDate = new_carddate
        cursor = cursor
        query = ("UPDATE Users SET cardDate=%s WHERE userID =%s")
        cursor.execute(query, (new_carddate, self.userID,))
        mydb.commit()
    def delete(self, cursor, mydb):
        userInput = input("To continue, please enter your password: ")
        continuer = self.checkPassword(userInput, self.userID)
        if (continuer):
            while(1):
                userInput = input("Are you sure you want to delete your account: ")
                if (userInput == "y" or "Y"):
                    print("Deleting your account from the system.")
                    cursor = cursor
                    query = "DELETE FROM Users WHERE userID=?"
                    cursor.execute(query, self.userID)
                    mydb.commit()
                    print(cursor.rowcount, "Account deleted successfully.")
                    print()
                    break
                elif (userInput == "n" or "N"):
                    print("Aborting deletion.")
                    break
                else:
                    print("Invalid input, please try again")
        else:
            print("Incorrect password. Please try again")
        def checkPassword(self, userInput, userID):
            while (1):
                userInput = input("Enter your password. Type 'abort' to exit this process. ")
                query = ("SELECT password FROM Users WHERE userID = %s")
                cursor.execute(query, (userID,))
                correctPassword = cursor.fetchall()
                if(correctPassword[0] == userInput):
                    break
                elif(userInput == 'abort'):
                    return 1
                else:
                    print("Invalid password. Please try again.")
            return (userInput == correctPassword[1])