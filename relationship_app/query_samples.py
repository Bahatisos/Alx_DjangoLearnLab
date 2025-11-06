from relationship_app.models import Author, Book, Library, Librarian

# Create some data
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(
    title="Harry Potter and the Sorcerer's Stone", author=author2)

library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

library1.books.add(book1, book2)
library2.books.add(book3)

librarian1 = Librarian.objects.create(name="Mr. Smith", library=library1)
librarian2 = Librarian.objects.create(name="Ms. Jane", library=library2)

# --- Required Queries ---

# 1️⃣ Query all books by a specific author
author_books = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", list(
    author_books.values_list("title", flat=True)))

# 2️⃣ List all books in a library
library_books = library1.books.all()
print(f"Books in {library1.name}:", list(
    library_books.values_list("title", flat=True)))

# 3️⃣ Retrieve the librarian for a library
librarian = library1.librarian
print(f"Librarian for {library1.name}:", librarian.name)
