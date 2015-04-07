'''Use object-oriented Python to model a public library (w/ three classes:
Library, Shelf, & Book). The library should be aware of a number of shelves.
Each shelf should know what books it contains. Make the book object have
"enshelf" and "unshelf" methods that control what shelf the book is sitting on.
The library should have a method to report all books it contains.

Note: this should *not* be a Django (or any other) app - just a single file
with three classes (plus commands at the bottom showing it works) is all that
is needed. In addition to pushing this python file to your Github account,
please also setup a http://repl.it/languages/Python (so it runs there) and
enter the saved URL here.'''


class Book(object):
    books = {}

    def __init__(self, book_name, book_shelf_num):
        self.book_name = book_name
        self.book_shelf_num = book_shelf_num

    def enshelf(self, book_name, book_shelf_num):
        """Add a book to a shelf"""

        if book_name not in self.books:
            self.books[book_name] = book_shelf_num
            print book_name + " added."
        else:
            print book_name + " its already on the shelf."

    def unshelf(self, book_name, book_shelf_num):
        """Remove a book from shelf"""
        if book_name in self.books:
            del self.books[book_name]
            print book_name + " removed."
        else:
            print book_name + " is not on the shelf"

    def changeshelf(self, book_name, book_shelf_num):
        """Change the location of the book"""

        if book_name not in self.books:
            self.books[book_name] = book_shelf_num
            print book_name + " added."
        else:
            self.books[book_name].update(book_shelf_num)
            print book_name + " location has been updated."


class Library(Book):

    def __init__(self, book_name, book_shelf_num, book_status='Checked In'):
        super(Library, self).__init__(self, book_name)
        self.book_shelf_num = 50
        self.book_status = book_status

# Shelf


def display_all_books(self):
    print "Title , Book Shelf Number:"
    print self.books.items()


class Shelf(Book):
    books = {}

    def __init__(self, book_name, book_shelf_num=1,
                 book_status='Checked In',
                 rack_number=1,
                 book_genre=' Classics'):
        super(Shelf, self).__init__(self, book_name)
        self.rack_number = rack_number
        self.book_genre = book_genre

    def shelf_book_lookup(self, x):

        for k, v in self.books.iteritems():
            if x == v:
                print "Books on the shelf you entered:"
                print '%s: %s' % (k, v)
            else:
                print "No Books on that shelf"


if __name__ == "__main__":

    # Check to see if this instance of Library knows how
    # Its not clear from the problem so preset the number
    # of shekves because a library can only have so many shelves
    # in it.

    UW_library = Library(book_name="X men volume 1",
                         book_shelf_num=2,
                         book_status="To be shelved")

    print UW_library.book_shelf_num

    print "Each Shelf should know what book it has:"
    print "Lets create an instance of Shelf first"
    my_shelved_books = Shelf(book_name="Tom Sawyer part 3")
    my_shelved_books = Shelf(book_name="Huck Finn part 4")
    my_shelved_books = Shelf(book_name="Superman Vol 10")

    print "Next lets load the Shelf with some books"

    my_shelved_books.enshelf("Tom Sawyer part 3", 7)
    my_shelved_books.enshelf("Huck Finn part 4", 7)
    my_shelved_books.enshelf("Superman Vol 10", 7)

    my_shelved_books.shelf_book_lookup(7)
    my_shelved_books.shelf_book_lookup(3)

    # Library should be able to print all books
    # First lets create an instance of library

    my_lib_books = Library(book_name="Tom Sawyer part 2", book_shelf_num=4)
    my_lib_books = Library(book_name="Huck Finn part 3", book_shelf_num=4)
    my_lib_books = Library(book_name="Superman Vol 9", book_shelf_num=2)

    # Next lets load the library with some books

    my_lib_books.enshelf("Tom Sawyer part 2", 4)
    my_lib_books.enshelf("Huck Finn part 3", 4)
    my_lib_books.enshelf("Superman Vol 9", 2)

    print display_all_books(my_lib_books)

    # Add books to shelfs

    mybooks = Book(book_name="Tom Sawyer", book_shelf_num=4)
    mybooks = Book(book_name="Huck Finn", book_shelf_num=4)
    mybooks = Book(book_name="Superman Vol 8", book_shelf_num=2)

    mybooks.enshelf("Tom Sawyer", 4)
    mybooks.enshelf("Huck Finn", 4)
    mybooks.enshelf("Superman Vol 8", 2)

    # remove books from shelfs

    mybooks.unshelf("Tom Sawyer", 4)
    mybooks.unshelf("Huck Finn", 4)
    mybooks.unshelf("Superman Vol 8", 2)

    # change the shelf a book is on

    # my_book1 = Library(book_name="X men vol 01", book_status="To be shelved")
    # my_book2 = Library(book_name="X men vol 02", book_status="Checkout")
    # my_book3 = Library(book_name="X men vol 03", book_status="Checkout")

    # my_book4 = Shelf(shelf_num=4, rack_number=1)
    # # my_book2 = Shelf(shelf_num=4, rack_number=1)
    # my_book3 = Shelf(shelf_num=5, rack_number=1)

    # print book_lookup(my_book1)
