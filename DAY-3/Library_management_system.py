class Library:
    def __init__(self):
        self.file = "books.txt"
    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        with open(self.file, "a") as f:
            f.write(f"{title},{author},Available\n")
        print("Book Added Successfully!")
    def view_books(self):
        try:
            with open(self.file, "r") as f:
                books = f.readlines()
                if len(books) == 0:
                    print("No Books Found")
                else:
                    print("\nBooks List")
                    for book in books:
                        print(book.strip())
        except FileNotFoundError:
            print("No Record Found.")
    def search_book(self):
        title = input("Enter Book Title: ")
        found = False
        try:
            with open(self.file, "r") as f:
                for book in f:
                    if title.lower() in book.lower():
                        print(book.strip())
                        found = True
            if not found:
                print("Book Not Found.")
        except FileNotFoundError:
            print("File Not Found.")
    def issue_book(self):
        title = input("Enter Book Title: ")
        books = []
        found = False
        try:
            with open(self.file, "r") as f:
                books = f.readlines()
            with open(self.file, "w") as f:
                for book in books:
                    if title.lower() in book.lower() and "Available" in book:
                        book = book.replace("Available", "Issued")
                        found = True
                    f.write(book)
            if found:
                print("Book Issued Successfully.")
            else:
                print("Book Not Available.")
        except FileNotFoundError:
            print("File Not Found.")
    def return_book(self):
        title = input("Enter Book Title: ")
        books = []
        found = False
        try:
            with open(self.file, "r") as f:
                books = f.readlines()
            with open(self.file, "w") as f:
                for book in books:
                    if title.lower() in book.lower() and "Issued" in book:
                        book = book.replace("Issued", "Available")
                        found = True
                    f.write(book)
            if found:
                print("Book Returned Successfully.")
            else:
                print("Book Not Found.")
        except FileNotFoundError:
            print("File Not Found.")
library = Library()
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.issue_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")