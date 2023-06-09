my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def bookList(bookDictionary):
    newBook = f"{bookDictionary['author']} wrote {bookDictionary['title']} in {bookDictionary['year']}. The book has {bookDictionary['pages']} pages and a rating of {bookDictionary['rating']}."
    return newBook
# print(bookList(my_book))
# print(type(bookList(my_book)))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_info():
    def book_title(bookDictionary):
        title = f"The title is {bookDictionary['title']}."
        return title
    # print(book_title(my_book))

    def book_author(bookDictionary):
        author = f"The author is {bookDictionary['author']}."
        return author
    # print(book_author(my_book))
    
    def book_year(bookDictionary):
        year = f"The year is {bookDictionary['year']}."
        return year
    # print(book_year(my_book))
    
book_info()
# print(type(book_info()))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def add_type(bookDictionary):
   book_info = bookDictionary["Type"]="Fiction"
   return book_info
# print(add_type(my_book))
# print(my_book)

def delete_rating(bookDictionary):
    del my_book["rating"]
    return my_book
# print(delete_rating(my_book))

def library_home(dictionary, bookDictionary):
    home_library = dictionary["book1"] = bookDictionary
    return home_library

home_library = {}
their_book = {
    "title": "The Gunslinger",
    "author": "Stephen King",
    "year": "1982",
    "rating": "4.6",
    "pages": "288"
}
print(library_home(home_library, my_book))
print(library_home(home_library, their_book))