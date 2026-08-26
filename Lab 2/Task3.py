# Task#3:
# Library Book System (Class vs Instance Attributes):
# Create a Book class with:
# • Class attribute: library_name
# • Instance attributes: title, author
# Add a method display_book() and show how changing the class attribute affects all objects.

class Book:
    library_name = "Fast Library"
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_book(self):
        print(f"Title: {self.title}, Author: {self.author}, Library: {self.library_name}")

b1 = Book("Harry Potter", "J.K Rowling")
b2 = Book("The Lord of the Rings", "J.R.R. Tolkien")

b1.display_book()
b2.display_book()
print("Changing Library Name for Book")
Book.library_name = "CS Library"
b1.display_book()
b2.display_book()
