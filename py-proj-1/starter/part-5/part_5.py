### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# # Code here
with open("library.txt", "w") as f:
    f.write("title, author, year, rating, pages\n")
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
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

fav_books = ["{'title': 'The Perfect Shadow', 'author': 'Brent Weeks', 'year': 2011, 'rating': 5.0, 'pages': 144}"]

def main_menu():
    active = True
    while active:
        answer = input("Press 1 to Enter a New Book, Press 2 to See All Books, Press any other key to exit menu. ")
        if answer == "1":
            new_book = create_book()
            with open("library.txt", "a") as f:
                f.write(f"{new_book['title']}, {new_book['author']}, {new_book['year']}, {new_book['rating']}, {new_book['pages']}\n") 
        elif answer == "2":
            print(fav_books)                
        else:   
            active = False
        
main_menu()

with open("library.txt", "r") as f:
    file = f.readlines()
    
    for line in file:
       title, author, year, rating, pages = line.split(", ")
       
       book_dictionary = {
           "title": title,
           "author": author,
           "year": int(year),
           "rating": float(rating),
           "pages": int(pages)
       }

if __name__ == "__main__":
        main_menu()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

