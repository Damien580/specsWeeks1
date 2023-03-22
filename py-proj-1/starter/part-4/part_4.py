### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_book():
#     book_title = input("What's your favorite book? ")
#     book_author = input("Who wrote your favorite book?")
#     book_year = input("What year was your favorite book published? ")
#     book_rating = input("What's the rating of your favorite book ")
#     book_pages = input("How many pages does your favporite book have? ")
    
#     book_dictionary = {
#         "title": book_title,
#         "author": book_author,
#         "year": book_year,
#         "rating": book_rating,
#         "pages": book_pages
#     }
    
#     return book_dictionary

# print(create_book())
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_book():
#     book_title = input("What's your favorite book? - ")
#     book_author = input("Who wrote your favorite book? - ")
#     book_year = int(input("What year was your favorite book published? - "))
#     book_rating = float(input("What's the rating of your favorite book - "))
#     book_pages = int(input("How many pages does your favporite book have? - "))
    
#     book_dictionary = {
#         "title": book_title,
#         "author": book_author,
#         "year": book_year,
#         "rating": book_rating,
#         "pages": book_pages
#     }
    
#     return book_dictionary

# print(create_book())

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# try:
#     book_year = int(input("What year was your favorite book published? - "))
# except: 
#      book_year = int(input("Please type a number for the year? - "))
     
### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# fav_books = ["Wizard and Glass", "Ender's Game", "Dune", "The Perfect Shadow"]

# new_book = input("What is the book you want to add? ")
# see_all = input("Would you like to see all available books? ")
# user_exit = input("Would you like to exit menu?")

# if type(new_book) == str :
#     fav_books.append(new_book)
# else: 
#     print(input("Please try again."))
    
# if see_all.lower() == "yes" or see_all.lower() == "y":
#     print(fav_books)
# elif see_all.lower() == "no" or see_all.lower() == "n":
#     print("Thank you.")
    


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
fav_books = ["Wizard and Glass", "Ender's Game", "Dune", "The Perfect Shadow"]

def main_menu():
    active = True
    while active:
        answer = input("Press 1 to Enter a New Book, Press 2 to See All Books, Press 3 to exit menu. ")
        if answer == "1":
            new_book = input("What is the book you want to add? ")
            fav_books.append(new_book)
        elif answer == "2":
            # see_all = input("Would you like to see all available books? ")
            print(fav_books)                
        else:   
            active = False
        
main_menu()