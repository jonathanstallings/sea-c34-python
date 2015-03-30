# What's your name?
def name_input(name):
    """
    Prompt for the user's name and print a greeting.
    Args:
        input1: string of user's first name
    Return:
        print a statement greeting the user
    """
    if (name.isalpha() is True):
        print("Hi, %s!" % name.title())
    else:
        print "Sorry, I didn't get that. Please enter letters only."

input1 = raw_input("What's your first name? ")
name_input(input1)


# What's my bill cost?

def calc_bill():
    """
    Prompt for the cost of the meal and return the total cost with tax and tip.
    Args:
        None
    Return:
        Total cost of bill
    """
    meal = float(raw_input("Enter cost of meal: "))
    tax = 0.095
    tip = 0.15
    meal = meal + meal * tax
    total = meal + meal * tip
    return total

print("Total Cost: %.2f" % calc_bill())


# Can you translate to pyg latin?
def pyg_translator():
    """
    Prompt user for word and return the pyg latin translation
    Args:
        None
    Return:
        Print pyg translation of word
    """
    pyg = "ay"
    user_word = raw_input("Enter word to be translated: ")

    if len(user_word) > 0 and user_word.isalpha():
        word = user_word.lower()
        first_letter = word[0]
        pyg_translation = word[1:len(word)] + first_letter + pyg
        print("Translation: %s" % pyg_translation.title())
    else:
        print "Sorry, you must enter a word with only letters."
        pyg_translator()

pyg_translator()
