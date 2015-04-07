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

# In order for it to work on python 2 and 3


class Book(object):
    def __init__(self, **kwargs):
        self.book_name = kwargs.get('book_name', 'Tom Sawyer')
        self.book_author = kwargs.get('book_author', 'Mark Twain')
        self.book_year = kwargs.get('book_year', '1945')
        self.book_publisher = kwargs.get('book_publisher', 'Westing House')
        self.shelf_num = kwargs.get('shelf_num', 1)
        self.book_status = kwargs.get('book_status', 'Checked In')

#         # shelf number
#         # status
#         def enshelf():
#             #add a book_name to a shelf_num , status checked in

#         def unshelf():
#             #take a book name and


class Library(Book):
    def __init__(self, **kwargs):

        # lib_books = {self.book_name: Book.book_author}

        self.book_name = kwargs.get('book_name', 'Tom Sawyer')
        self.shelf_num = 50
        self.book_status = kwargs.get('book_status', 'Checked In')

        # #variables
        # # self
        # book_name
        # shelf_num
        # methods
        # count number of shelves:  number of values, or range
        # print all books
        # pass
#     # Shelf


def print_all_books(self):
    print self.lib_books.items()


class Shelf(Book):
    def __init__(self, **kwargs):
        self.rack_number = kwargs.get('rack_number', '1')
        self.book_genre = kwargs.get('book_genre', 'Classics')

# method enter book and find its shelf number


def book_lookup(self):
    print "Book Name:"
    print self.book_name.upper()
    print "Shelf Number:"
    print self.shelf_num


# def book_shelf_lookup(self):
#     # Enter a Book


if __name__ == "__main__":

    my_book1 = Library(book_name="X men vol 01", book_status="To be shelved")
    my_book2 = Library(book_name="X men vol 02", book_status="Checkout")
    my_book3 = Library(book_name="X men vol 03", book_status="Checkout")

    all_books = Library()

    # my_book4 = Shelf(shelf_num=4, rack_number=1)
    # # my_book2 = Shelf(shelf_num=4, rack_number=1)
    # my_book3 = Shelf(shelf_num=5, rack_number=1)

    print book_lookup(my_book1)

