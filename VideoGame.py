class VideoGame:
    # VideoGame class constructor
    def __init__(self, title, developer, release_year, console, gameID, price, in_stock):
        self.title = title
        self.developer = developer
        self.release_year = release_year
        self.console = console
        self.gameID = gameID
        self.in_stock = in_stock
        self.price = price
    # function to display video game attributes
    def viewInfo(self):
        print(f"Title: {self.title}\n"
              f"Developer: {self.developer}\n"
              f"Console: {self.console}\n"
              f"Game ID: {self.gameID}\n"
              f"Number of copies in stock: {self.in_stock}\n"
              f"Price: {self.price}\n")
    # function to set stock
    def setStock(self, new_stock):
        self.in_stock = new_stock
