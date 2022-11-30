class OrderHistory:
    def __init__(self, UserID, Title=None, GameID=None, Quantity=None):
        self.Title = Title
        self.GameID = GameID
        self.Quantity = Quantity
        self.UserID = UserID

    def viewOrderHistory(self, cursor):
        cursor = cursor
        query = ("SELECT * FROM orderhistory WHERE userID = %s")
        data = self.UserID
        cursor.execute(query, (data,))
        myresult = cursor.fetchall()
        i=1
        for x in myresult:
            print(str(i) + ". Title: " + x[0] + " --- " + x[2])
            print("\tQuantity: ", x[1])
            i+=1
