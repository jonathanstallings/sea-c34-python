'''The functions below perform ROT13 encryption on a string. The first
function converts a string to a list, splits each character up and iterates
it through a for loop and then converts its characters to rot13 encryption,
it accepts whitespace, and accepts punctuation'''


def rot13(x):

    '''The first function converts a string to a list, splits each character up
    and iterates it through a for loop and then converts its characters to
    rot13 encryption, it accepts whitespace, and accepts punctuation
    Arguments: A string. It will accept upper and lower case characters. It
    returns a rot13 encrypted string. It returns: a rot13 converted string
    '''

    # Create a dictonary that handles the conversion/encryption of letters. Add
    # a place at the end for whitespace. Based on the dictionary's size this
    # produces pep8 errors

    rot13_ids = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
                 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y',
                 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
                 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
                 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q',
                 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
                 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
                 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
                 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', ' ': ' '}

    # create an empty list to write our converted, concatenated results to
    s = ''
    results = list(s)

    # split letters up
    split_list = list(x)
    # interate through each character

    punctuation = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

    for id in split_list:
        # if a letter is a punctuation then add it
            if id in punctuation:
                results += "".join(id)
    # otherwise if its a whitespace or letter, lower or uppercase convert
    # with our dictonary above.
            else:
                results += "".join(rot13_ids[id])
    return results


def rot13_more_elegant(x):
    '''This performs rot13 encryption using the string module and maketrans
       Argurments: a string'''

    import string

    # Based on the size of this translation table we produce a pep8/lint error
    rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    print string.translate(x, rot13)

    # This produces no pep8 errors and is very elegant. it uses the codec package
def rot13_very_elegant(x):
    import codecs
    print codecs.encode(x, 'rot_13')

if __name__ == '__main__':
    # lets start out simple with a couple of letters
    print(rot13('ab'))
    # # lets add a space and a capital letter
    print(rot13(' R'))
    # # lets test punctuation
    print(rot13('%$abcdefghi'))
    # # lets test lowercase and punctuation
    print(rot13('rich%'))
    # # lets test upper and lower case
    print(rot13('R i c h '))
    # # lets test upper and lower case again
    print(rot13('Code'))
    # lets test all upper case
    print(rot13('FELLOWS'))
    # Lets add some assert statements
    assert(rot13('FELLOWS') == ['S', 'R', 'Y', 'Y', 'B', 'J', 'F'])
    # Lets try a more elegant version
    print(rot13_more_elegant('rich%'))
    # And and even more elegant encryption
    print(rot13_very_elegant('R i c h '))
