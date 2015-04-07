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

# 3 classes library shelf and book


# Library
class Library(object):
''' method: print all books'''
''' record number of shelves'''
''' shelf should have books'''
'''add up books and report their number'''


num_of_shelves = 0


def __init__(self,book.name, shelf_num):

self.numofshelves = num_of_shelves
self.booknames = book_names


# Shelf
class Shelf(object):
''' record number of shelves'''
''' shelf should have books'''

book_name

def __init__(self,book.name,shelf.num):
print(book.name)



# Book
class Book(object):

    def __init__(self,book, shelf):

    def enshelf(self, book, shelf):
        """Add book to the shelf."""
        if book not in self:
            self[book] = shelf
            print book + " added."
        else:
            print book + " is already on the shelf." + shelf

    #         if name in donor_info:
    #     donor_info[name].append(float(donation_amount))
    # else:
    #     donor_info[name] = [float(donation_amount)]


    def unshelf:(book.name, shelf.num, status)
    print " Book is on shelf:" % (x)
