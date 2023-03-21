### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["Stephen King", "J. R. R. Tolkien", "George R. R. Martin", "Patrick Rothfuss", "Barndon Sanderson", "Doug Adams", "Alfred Hitchcock", "Poppy Z. Brite"]

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append("Tom Clancy")
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

my_authors.remove("J. R. R. Tolkien")
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[3]
# Example: my_authors[2]


# Now slice the list.

my_authors[6:8]
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_author_tuple = ("Stephen King", "J. R. R. Tolkien", "George R. R. Martin", "Patrick Rothfuss", "Barndon Sanderson", "Doug Adams", "Alfred Hitchcock", "Poppy Z. Brite")
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

my_author_set = {"Stephen King", "J. R. R. Tolkien", "George R. R. Martin", "Patrick Rothfuss", "Barndon Sanderson", "Doug Adams", "Alfred Hitchcock", "Poppy Z. Brite"}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

my_author_set.add("Terry Brooks")
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

my_author_set.add("Terry Brooks")
print(my_author_set)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for author in my_authors:
    print(author)
    
for author in my_author_tuple:
    print(author)
    
for author in my_author_set:
    print(author)
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

