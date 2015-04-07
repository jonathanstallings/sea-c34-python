# list_lab.py

# build new fruit basket
fruit_basket = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

# display fruit from fruit basket
print u"Your fruit basket has %s" % fruit_basket

# ask user to add a new fruit to fruit basket
new_fruit = raw_input(u'Please enter a fruit for the fruit basket-->')

# add new fruit to fruit basket
fruit_basket.append(new_fruit)

# display fruit from fruit basket
print u"Your fruit basket has %s" % fruit_basket

# ask user for a number
fruit_number = raw_input(u'Please enter a number between 1-5-->')

# display fruit from fruit basket
print u"Number %s fruit out of your Your fruit basket is %s" % (fruit_number, fruit_basket[fruit_number-1])

# Add another fruit to the beginning of the list using “+” and display the list.
fruit_basket = [u"Mangos"] + fruit_basket

# Add another fruit to the beginning of the list using insert() and display the list.
fruit_basket.insert(0, u"Plums")

# Display all the fruits that begin with “P”, using a for loop.
for fruit in fruit_basket:
    first_letter = fruit[0]  # declear the first letter
    if first_letter.upper() == u"P":  # compare the first letter
        print fruit  # print fruit

# display fruit from fruit basket
print u"Your fruit basket has %s" % fruit_basket

# Remove the last fruit from the list.
fruit_basket.pop(len(fruit_basket)-1)

# Display the list.
print u"Your fruit basket has %s" % fruit_basket

# Ask the user for a fruit to delete and find it and delete it.(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
number_of_fruit = len(fruit_basket)


def delete_fruit_function():
    delete_fruit = raw_input(u'Which fruit would you like to delete-->')
    for fruit in fruit_basket:
        if fruit.lower() == delete_fruit.lower():
            fruit_basket.remove(fruit)

while len(fruit_basket) == number_of_fruit:
    delete_fruit_function()

#  Ask the user for input displaying a line like “Do you like apples?”
#  for each fruit in the list (making the fruit all lowercase).
#  For each “no”, delete that fruit from the list.
#  For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
for fruit in fruit_basket:
    answer = raw_input(u'Do you like %s?-->' % fruit.lower())
    print answer.lower()
    while answer.lower() != "no" and answer.lower() != "yes":
        answer = raw_input(u'Do you like %s?-->' % fruit.lower())
        if answer.lower() == "no":
            fruit_basket.remove(fruit)
            break
        elif answer.lower() == "yes":
            break

#  Display the list.
print fruit_basket

# Make a copy of the list and reverse the letters in each fruit in the copy.
reverseletters_fruit_basket = []

for fruit in fruit_basket:
    reverseletters_fruit = ""
    for letter in fruit:
        reverseletters_fruit = letter+reverseletters_fruit
    reverseletters_fruit_basket.append(reverseletters_fruit)

# Delete the last item of the original list. Display the original list and the copy.
fruit_basket.remove(len(fruit_basket-1))

print fruit_basket
print reverseletters_fruit_basket
