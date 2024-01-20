class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Author:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name):
        self.name = name

# Usage example
author1 = Author("John Doe")
book1 = Book("Book 1", author1)
user1 = User("Alice")

print(f"Book: {book1.title} by {book1.author.name}")
print(f"User: {user1.name}")
