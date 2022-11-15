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

    def setfname(self, new_fname):
        self.fname = new_fname
    def setlname(self, new_lname):
        self.lname = new_lname
    def setstreet(self, new_street):
        self.street = new_street
    def setcity(self, new_city):
        self.city = new_city
    def setstate(self, new_state):
        self.state = new_state
    def setzip(self, new_zip):
        self.zip = new_zip
    def setusername(self, new_name):
        self.username = new_name
    def setpassword(self, new_password):
        self.password = new_password
    def setemail(self, new_email):
        self.email = new_email
    def settelephone(self, new_phone):
        self.telephone = new_phone
    def setcardnum(self, new_cardnum):
        self.cardNum = new_cardnum
    def setcvv(self, new_cvv):
        self.cvv = new_cvv
    def setcardname(self, new_cardname):
        self.cardName = new_cardname
    def setcarddate(self, new_carddate):
        self.cardDate = new_carddate

#delete should probably be built as a class funtion as well
#functions to grab from SQL to build user, setters including writing to the DB
#setters for fname, lname, street, city, state, zip, uname, password, email, telephone, cardNum, cvv, cardName, cardDate
