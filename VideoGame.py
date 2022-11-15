class VideoGame:
    def __init__(self, title, developer, release_year, console, gameID, in_stock):
        self.title = title
        self.developer = developer
        self.release_year = release_year
        self.console = console
        self.gameID = gameID
        self.in_stock = in_stock

    def viewInfo(self):
        print(f"Title: {self.title}\n"
              f"Developer: {self.developer}\n"
              f"Console: {self.console}\n"
              f"Game ID: {self.gameID}\n"
              f"Number of copies in stock: {self.in_stock}\n")

    def setStock(self, new_stock):
        self.in_stock = new_stock