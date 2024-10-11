# Python Class book
class book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = int(publication_year)
    def __str__(self):
        return f"title: {self.title}, author{self.author}, publication_year{self.publication_year}"
if __name__ == "__main__":
    title = input("enter the title of the book: ")
    author = input("enter the author name")
    publication_year = input("enter the publication year of the book: ")
# create the instance of the book
Book = book(title, author, publication_year)
print(Book)