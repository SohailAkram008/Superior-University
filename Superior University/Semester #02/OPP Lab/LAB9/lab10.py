import csv
class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")    
        print(f"Author: {self.author}")    
class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")


def save_to_file(filename, data, headers):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"Data saved to {filename}")

def read_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [row for row in reader if row]
        return headers, data

def menu():
    while True:
        print(f"\nChoose from the Following:")
        print("1 for Book")
        print("2 for Article")
        print("3 to Exit")
        user_input = input("Waiting for input: ")
        
        if user_input == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            pages = input("Enter the number of pages: ")
            book = [title, author, genre or None, pages or None]
            save_to_file("books.csv", book, ["Title", "Author", "Genre", "Pages"])
        
        elif user_input == "2":
            title = input("Enter the article title: ")
            author = input("Enter the article author: ")
            journal = input("Enter the journal name: ")
            doi = input("Enter the DOI: ")
            article = [title, author, journal or None, doi or None]
            save_to_file("articles.csv", article, ["Title", "Author", "Journal", "DOI"])
        elif user_input == "3":
            print("Exiting program.")
            break
        
        else:
            print("Incorrect user input.")

menu()
