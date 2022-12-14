class Cart:
    def __init__(self, UserID, Title=None, GameID=None, Quantity=0):
        self.Title = Title
        self.GameID = GameID
        self.Quantity = Quantity
        self.UserID = UserID

# View items in your cart
    def viewCart(self, cursor):
        cursor = cursor
        query = ("SELECT * FROM cart WHERE userID = %s")
        data = self.UserID
        cursor.execute(query, (data,))
        myresult = cursor.fetchall()
        print ("Your Cart: \n")
        for x in myresult:
            print("Title: " + x[0] + " --- " + x[2])
            print("\tQuantity: ", x[1])

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
# adds games to cart using a VideoGame object
    def insertCart(self,cursor,mydb):
        cursor = cursor
        query = ("SELECT Quantity FROM inventory WHERE GameID = %s")
        cursor.execute(query,(self.GameID,))
        stock = cursor.fetchone()
        lst = list(stock)
        tmp = lst[0]
        tmp = int(tmp) - self.Quantity
        lst[0] = tmp
        stock = tuple(lst)
        query = ("UPDATE inventory SET Quantity = %s WHERE GameID = %s")
        cursor.execute(query, (stock[0], self.GameID,))
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
        numID = cursor.fetchall()
        if numID == []:
            print("Invalid gameID. Please try again.")
            return False
        else:
            removeGame = numID[0][0]
            query = "SELECT Quantity FROM cart WHERE GameID = %s"
            cursor.execute(query, (removeGame,))
            cartQuan = cursor.fetchall()
            query = "DELETE FROM cart WHERE GameID = %s"
            cursor.execute(query, (removeGame,))
            query = "SELECT Quantity FROM inventory WHERE GameID = %s"
            cursor.execute(query, (removeGame,))
            stock = cursor.fetchone()
            lst = list(stock)
            tmp = lst[0]
            cartQuan = list(cartQuan)
            quan = cartQuan[0][0]
            quan = int(quan)
            tmp = int(tmp) + quan
            lst[0] = tmp
            stock = tuple(lst)
            query = "UPDATE inventory SET Quantity = %s WHERE GameID = %s"
            cursor.execute(query, (stock[0], removeGame))
            mydb.commit()
            return True

# Clears cart database and adds everything to order history
    def checkout(self, cursor, mydb):
        cursor = cursor
        query = "SELECT GameID FROM cart WHERE UserID = %s"
        data = self.UserID
        cursor.execute(query, (data,))
        numID = cursor.fetchall()

        if numID == []:
            print("There is nothing in your cart.")
        else:
            while(True):
                confirm = int(input("Are you sure you wish to checkout? \n1. Yes \n2. No\n Enter a number to select an option: "))
                if (confirm == 2):
                    return False
                elif (confirm == 1):
                    break
                else:
                    print("Invalid input, please try again.")
            query = "DELETE FROM cart WHERE UserID = %s"
            cursor.execute(query, (data,))
            mydb.commit()

