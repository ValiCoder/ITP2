class Book:
    def __init__(self, id, title, price, available=True):
        self.__id = id
        self.__title = title
        self.__price = price
        self.__available = available

    def __str__(self):
        availability = "Available" if self.__available else "Not available at the moment"
        return f"ID: {self.__id}, Title: '{self.__title}', Price: ${self.__price:.2f}, Status: {availability}"

    def applyDiscount(self, discount_percentage):
        discount_amount = self.__price * (discount_percentage / 100)
        self.__price -= discount_amount

    def availabilitySwitch(self):
        self.__available = not self.__available

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @property
    def available(self):
        return self.__available


class EBook(Book):
    def __init__(self, id, title, price, file_size, available=True):
        super().__init__(id, title, price)
        self.__file_size = file_size
        self.__available = True

    def __str__(self):
        return super().__str__() + f", File Size: {self.__file_size}MB"

    @property
    def fileSize(self):
        return self.__file_size


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def displayBooks(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def borrowBook(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.available:
                    book.availabilitySwitch()
                    print(f"Book '{book.title}' borrowed successfully!")
                    return
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                    return
        print("Book not found.")

    def returnBook(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if not book.available:
                    book.availabilitySwitch()
                    print(f"Book '{book.title}' returned successfully!")
                    return
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                    return
        print("Book not found.")

    def discount(self, discount_percentage):
        for book in self.books:
            book.applyDiscount(discount_percentage)

    def getNextId(self):
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1


def sort_books_by_price(books, ascending=True):
    return sorted(books, key=lambda x: x.price, reverse=not ascending)


def find_books_by_title(keyword, books):
    return list(filter(lambda x: keyword.lower() in x.title.lower(), books))


def main():
    library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Apply Discounts")
        print("6. Search for Books by Title")
        print("7. Sort Books by Price")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = library.books[-1].id + 1 if library.books else 1
            print("The Automatically Assigned ID:", book_id)

            title = input("Enter Book Title: ").strip()

            while True:
                try:
                    price = float(input("Enter Book Price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric price.")

            is_ebook = input("Is this an EBook? (yes/no): ").strip().lower()
            while True:
                if is_ebook == "yes":
                    while True:
                        try:
                            file_size = float(input("Enter File Size (MB): "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid file size.")
                    library.addBook(EBook(book_id, title, price, file_size))
                    break
                elif is_ebook == "no":
                    library.addBook(Book(book_id, title, price))
                    break
                else:
                    print("Sorry, didn't understand you. Please enter 'yes' or 'no'.")
                    is_ebook = input("yes/no ").strip().lower()

        elif choice == "2":
            library.displayBooks()

        elif choice == "3":
            while True:
                try:
                    book_id = int(input("Enter Book ID to Borrow: "))
                    library.borrowBook(book_id)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid Book ID.")


        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID to Return: "))
                library.returnBook(book_id)
            except ValueError:
                print("Invalid input. Please enter a valid Book ID.")

        elif choice == "5":
            while True:
                try:
                    discount = float(input("Enter discount percentage (e.g., 10 for 10%): "))
                    if 0 <= discount <= 100:
                        break
                    else:
                        print("Please enter a percentage between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a discount percentage.")

            library.discount(discount)
            print(f"Discount of {discount}% applied to all books.")

        elif choice == "6":
            keyword = input("Enter Keyword to Search: ").strip()
            results = find_books_by_title(keyword, library.books)
            if results:
                print("Books matching your search:")
                for book in results:
                    print(book)
            else:
                print("No books found with that title.")

        elif choice == "7":
            while True:
                order = input("Sort by Price (asc/desc): ").strip().lower()

                if order == "asc":
                    ascending = True
                    break
                elif order == "desc":
                    ascending = False
                    break
                else:
                    print("Sorry, didn't understand you. Please enter 'asc' or 'desc'.")

            sorted_books = sort_books_by_price(library.books, ascending=ascending)
            print("Books sorted by price:")
            for book in sorted_books:
                print(book)

        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

        doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()
        while True:
            if doNext == "yes":
                print("Continuing with the operation...\n")
                break
            elif doNext == "no":
                print("Exiting the Library Management System. Thank you!")
                return
            else:
                print("Sorry, didn't understand you, please enter 'yes' or 'no'")
                doNext = input("\nDo you want to continue? (yes/no): ").strip().lower()


if __name__ == "__main__":
    main()
