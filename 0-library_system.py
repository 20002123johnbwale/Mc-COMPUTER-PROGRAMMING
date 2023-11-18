class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def checkout_book(self, member, book):
        if book in self.books and member in self.members:
            if not book.checked_out:
                book.checked_out = True
                book.borrower = member
                member.borrowed_books.append(book)
                print(f"Book '{book.title}' has been checked out by {member.name}.")
            else:
                print(f"Book '{book.title}' is already checked out.")
        else:
            print("Invalid book or member.")

    def return_book(self, member, book):
        if book in self.books and member in self.members:
            if book.checked_out and book.borrower == member:
                book.checked_out = False
                book.borrower = None
                member.borrowed_books.remove(book)
                print(f"Book '{book.title}' has been returned by {member.name}.")
            else:
                print(f"Book '{book.title}' is not checked out by {member.name}.")
        else:
            print("Invalid book or member.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
        self.borrower = None


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []