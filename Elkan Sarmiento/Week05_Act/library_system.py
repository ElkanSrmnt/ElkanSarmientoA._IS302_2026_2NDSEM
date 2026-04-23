class Book_eas:
    def __init__(self_eas, title_eas, author_eas, year_eas):
        self_eas.title_eas = title_eas
        self_eas.author_eas = author_eas
        self_eas.year_eas = year_eas
    
    def display_book_eas(self_eas):
        print("Title:", self_eas.title_eas)
        print("Author:", self_eas.author_eas)
        print("Year:", self_eas.year_eas)
        print()


print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_eas = Book_eas("Python Programming", "John Smith", 2022)
book2_eas = Book_eas("Data Science Basics", "Sarah Johnson", 2021)
book3_eas = Book_eas("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_eas.display_book_eas()

print("Book 2:")
book2_eas.display_book_eas()

print("Book 3:")
book3_eas.display_book_eas()