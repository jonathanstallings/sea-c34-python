# Q1 How to create a dictionary?


def states():
    """
    Create a dictionary with five key:value pairs

    Args:

    Returns: Dictionary items
    """
    states = {'California': 'Sacramento', 'Oregon': 'Salem', 'Florida': 'Talahasee', 'Texas': 'Austin', 'Boise': 'Idaho'}
    print states

states()


# Q2 How to index a dictionary?

def statesindex():
    """
    Indexing a dictionary by key

    Args:

    Returns: Dictionary items
    """
    states = {'California': 'Sacramento', 'Oregon': 'Salem', 'Florida': 'Talahasee', 'Texas': 'Austin', 'Boise': 'Idaho'}

    print states['California']
    print states['Salem']
    print states['Talahasee']
    print states['Austin']
    print states['Boise']

statesindex()

# Q3 Can a tuple containing a list go inside of a dictionary?


def listtupledict():
    """
    Inserting a list inside of a tuple inside of a dictionary

    Args:

    Returns: String
    """

    list = [5, 4, 3, 2, 1]
    tuple = ('A', 'B', 'C', 'D', list)

    try:
        dict = {'Do', 'Rae', 'Me', 'Fa', tuple}
    except:
        print "Can't do that!"

listtupledict()

# Q4 How to iterate through items of a dictionary?


def statesiteration():
    states = {'California': 'Sacramento', 'Oregon': 'Salem', 'Florida': 'Talahasee','Texas': 'Austin', 'Boise': 'Idaho'}
    for k, v in states.items():
        print("%s: %s" % (k, v))

statesiteration()
