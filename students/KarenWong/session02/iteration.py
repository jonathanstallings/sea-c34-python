def get_index():

    """
    How to take an iteratable and get the index?

    """
list(enumerate(["p", "y", "t", "h", "o", "n"]))
for i, c in enumerate(["p", "y", "t", "h", "o", "n"]):
        print i, c


def devowel():

    """
    How to remove vowels from words?

    """
food_names = ["Pasta", "Apple", "Seafood", "Potato"]
vowels = list('aeiou')
output = []

for food in food_names:
    food_list = list(food.lower())

    for vowel in vowels:
        while True:
            try:
                food_list.remove(vowel)
            except:
                break
    output.append(''.join(food_list).capitalize())

print(output)


def pass_statement():
    """
    How do you write a command that does not execute?

    """
    for letter in "Monday":
        if letter == "n":
            pass
            print "I don't want this block to execute"
        print "I am the letter :", letter
