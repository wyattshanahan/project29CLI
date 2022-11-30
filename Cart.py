class Cart:
    def __init__(self, Title, GameID, Quantity, UserID):
        self.Title = Title
        self.GameID = GameID
        self.Quantity = Quantity
        self.UserID = UserID

# View items in your cart
    def viewCart(self):
        print("Cart:\n")
        print("Title: " + self.Title + " --- " + self.GameID)
        print("Quantity : " + self.Quantity)

# Adds game to your cart SQL table
    def addCart(self, cursor, mydb):
        cursor = cursor
        userInput = input("Enter the gameID of the game you would like to buy: ")
        #query = "SELECT GameID FROM inventory WHERE GameID = %s"
        #cursor.execute(query, (userInput,))
        numID = userInput

        query = "SELECT Title FROM inventory WHERE GameID = %s"
        cursor.execute(query, (numID,))
        title = cursor.fetchone()

        query = "SELECT Quantity FROM inventory WHERE GameID = %s"
        cursor.execute(query, (numID,))
        stock = cursor.fetchone()
        stock = stock - 1
        query = "UPDATE inventory SET Quantity = %s WHERE GameID = %s"
        cursor.execute(query, (stock, numID,))

        cart = (title, 1, numID)
        query = "INSERT INTO cart (Title, Quantity, GameID, UserID) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (cart,))
        mydb.commit()

    def insertCart(self,cursor,mydb):
        cursor = cursor
        query = ("SELECT Quantity FROM inventory WHERE GameID = %s")
        cursor.execute(query,(self.GameID,))
        stock = cursor.fetchone()
        stock = stock[0][0]
        stock = int(stock)
        stock -= self.Quantity
        query = ("UPDATE inventory SET Quantity = %s WHERE GameID = %s")
        cursor.execute(query, (self.Quantity, self.GameID,))
        mydb.commit()
        newquery = ("INSERT INTO cart (Title, Quantity, GameID, UserID) VALUES (%s, %s, %s, %s)")
        data = (self.Title, self.Quantity, self.GameID, self.UserID)
        cursor.execute(newquery, data)
        mydb.commit()

# Removes game from the cart SQL table
    def removeCart(self, cursor, mydb):
        cursor = cursor
        userInput = input("Enter the gameID of the game you would like to remove from your cart: ")
        query = "SELECT GameID FROM inventory WHERE GameID = %s"
        cursor.execute(query, (userInput,))
        numID = cursor.fetchone()

        if numID == []:
            print("Invalid gameID. Please try again.")
        else:
            query = "DELETE FROM cart WHERE GameID = %s"
            cursor.execute(query, (numID,))

            query = "SELECT Quantity FROM inventory WHERE GameID = %s"
            cursor.execute(query, (numID,))
            stock = cursor.fetchone()
            stock = stock + 1
            query = "UPDATE inventory SET Quantity = %s WHERE GameID = %s"
            cursor.execute(query, (stock, numID,))
            mydb.commit()

# Clears cart database and adds everything to order history
    def checkout(self, cursor, mydb):
        cursor = cursor
        query = "SELECT GameID FROM cart WHERE UserID = %s"
        data = self.UserID
        cursor.exectue(query, (data,))
        numID = cursor.fetchall()

        if numID == []:
            print("There is nothing in your cart.")
        else:
            query = "SELECT Quantity FROM cart"
            cursor.exectue(query)
            stock = cursor.fetchall()

            query = "SELECT Title FROM cart"
            cursor.exectue(query)
            title = cursor.fetchall()

            history = (title, stock, numID)
            query = "INSERT INTO OrderHistory (Title, Quantity, GameID) VALUES (%s, %s, %s)"
            cursor.execute(query, (history,))
            mydb.commit()

