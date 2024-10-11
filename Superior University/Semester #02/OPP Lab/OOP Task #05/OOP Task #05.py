# SINGLE INHERITENCE
# Model a library System
# Parent class
class Item:
    def __init__(self,title,author):
        self.author = author
        self.title = title

    def display_info(self):
        print(f"Title {self.title}, Author{self.author}")

# Child class
class Book(Item):
    def __init__(self, title, author,page):
        super().__init__(title, author)
        self.page = page

    def more_info(self):
        print(f"Pages: {self.page}")

class Magzine(Item):
    def __init__(self, title, author,issue_number):
        super().__init__(title, author)
        self.Issue_number = issue_number

    def more_info(self):
        print(f"Issue number: {self.Issue_number}")

book = Book("Alchemist", "Paulo Coelho", 195)
magzine = Magzine("The Wall Street", "Romen Powell",1994)

book.display_info()
book.more_info()

magzine.display_info()
magzine.more_info()
    