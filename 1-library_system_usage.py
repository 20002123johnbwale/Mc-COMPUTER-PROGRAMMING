
# Create library and add books
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Add members
member1 = Member("John")
member2 = Member("Jane")
library.add_member(member1)
library.add_member(member2)

# Checkout books
library.checkout_book(member1, book1)
library.checkout_book(member2, book2)
# Attempt to borrow a book already checked out
library.checkout_book(member1, book2)

# Return books
library.return_book(member1, book1)
library.return_book(member2, book2)
library.return_book(member1, book2)  # Attempt to return a book not checked out

# Remove books and members
library.remove_book(book1)
library.remove_member(member1)
