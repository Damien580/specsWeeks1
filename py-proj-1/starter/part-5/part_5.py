### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# # Code here
# 
def create_book():
    book_title = input("What's your book titled? - ")
    book_author = input("Who wrote your book? - ")
    book_year = int(input("What year was new book published? - "))
    book_rating = float(input("What's the goodreads.com rating of your book? - "))
    book_pages = int(input("How many pages does your book have? - "))
    
    book_dictionary = {
        "title": book_title,
        "author": book_author,
        "year": book_year,
        "rating": book_rating,
        "pages": book_pages
    }
    
    return book_dictionary
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
book_source = "library.txt"

def get_books_as_list_of_dictionaries(book_source):
    books_list = []
    with open(book_source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def view_books(book_source):
    print("\nHere are all your books...\n")
    for books in get_books_as_list_of_dictionaries(book_source):
        get_book_printed(books)

def get_sorted_list_by_rating(book_source):
    print("\nHere are all your books ranked by rating...\n")
    list = get_books_as_list_of_dictionaries(book_source)
    list =  sorted(list, key=lambda x: int(x["rating"]), reverse = True)
    for book in list:
        get_book_printed(book)

def get_sorted_list_by_length(book_source):
    print(f"\nYour books from longest to shortest are...\n")
    list = get_books_as_list_of_dictionaries(book_source)
    list = sorted(list, key=lambda x: int(x["pages"]), reverse=True)
    for book in list:
        get_book_printed(book)
        
def get_sorted_list_by_year(book_source):
    print("\nYour books from oldest to newest are...\n")
    list = get_books_as_list_of_dictionaries(book_source)
    list = sorted(list, key=lambda x: int(x["year"]))
    for book in list:
        get_book_printed(book)   
def main_menu():
    active = True
    while active:
        choice = input("""
Choose 1 to add a book...
Choose 2 to see all your books...
Choose 3 to see book count...
Choose 4 to see books by length...
Choose 5 to see books by date published...
Choose any other key to exit...
Type here: """)
        
        if choice == "1":
            new_book = create_book()
            with open(book_source, "a") as f:
                f.write(f"{new_book['title']}, {new_book['author']}, {new_book['year']}, {new_book['rating']}, {new_book['pages']}\n") 
                
        elif choice == "2":
            view_books(book_source)
            
        elif choice == "3":
             print(f"\nYou have a total of {len(get_books_as_list_of_dictionaries(book_source))} books.\n")

        elif choice == "4":
            get_sorted_list_by_length(book_source)
        
        elif choice == "5":
            get_sorted_list_by_year(book_source)
            
        else:   
            active = False

if __name__ == "__main__":
        main_menu()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

