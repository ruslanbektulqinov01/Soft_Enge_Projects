class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added the book: {book.name}')

    def remove_book(self, book_name):
        found_book = None
        for book in self.books:
            if book.name == book_name:
                found_book = book
                break

        if found_book:
            self.books.remove(found_book)
            print(f'Removed the book: {found_book.name}')
        else:
            print(f'Book "{book_name}" not found in the library.')

    def search_with_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f'Books by {author}:')
            for book in found_books:
                print(f"'{book.name}' by {book.author}")
        else:
            print(f'No books found by {author} in the library.')

    def search_with_year(self, year):
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            print(f'Books published in {year}:')
            for book in found_books:
                print(f"'{book.name}' by {book.author}")
        else:
            print(f'No books found published in {year}.')


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.name}' by {self.author} ({self.year})"


def main():
    library = Library()
    while True:
        print("\n1. Add a book")
        print("2. Remove a book")
        print("3. Search books by author")
        print("4. Search books by year")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the book's name: ")
            author = input("Enter the author's name: ")
            year = int(input("Enter the year of publication: "))
            book = Book(name, author, year)
            library.add_book(book)
        elif choice == "2":
            book_name = input("Enter the book's name to remove: ")
            library.remove_book(book_name)
        elif choice == "3":
            author = input("Enter the author's name to search books: ")
            library.search_with_author(author)
        elif choice == "4":
            year = int(input("Enter the year to search books: "))
            library.search_with_year(year)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
