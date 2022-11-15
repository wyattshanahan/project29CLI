class User:
    def __init__(self, userID, fname, lname, street, city, state, userZip, username, password, email, telephone, cardNum, cvv, cardName,cardDate, orderNum):
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

#delete should probably be built as a class funtion as well
#functions to grab from SQL to build user, setters including writing to the DB
#setters for fname, lname, street, city, state, zip, uname, password, email, telephone, cardNum, cvv, cardName, cardDate
