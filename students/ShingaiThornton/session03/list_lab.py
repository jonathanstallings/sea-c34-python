
# !/Shingai/bin/env python


def fruitsprint():
    print fruits

# Create list of fruits
fruits = ['apples', 'pears', 'oranges', 'peaches']
fruitsprint()

# Ask user to input a new fruit
newFruit = raw_input("Enter a new fruit name:")
fruits.append(newFruit)
fruitsprint()

# Ask user for a number, print coresponding fruit
fruitNumber = raw_input("Pick a number:")
print fruitNumber + " " + fruits[int(fruitNumber) - 1] 

# Add fruit to list using "+"
fruits = fruits + ['papaya']
fruitsprint()

# Add frut to list using .insert()
fruits.insert(0, "guava")
fruitsprint()

# Print fruits starting with P
pFruits = fruits[:]

for fruit in pFruits[:]:
    if fruit[0] != "p":
        pFruits.remove(fruit)
print pFruits

# Remove last fruit from list, print result
fruitsprint()
lastFruitRemoved = fruits[:]
lastFruitRemoved.remove(lastFruitRemoved[-1])
print lastFruitRemoved

# Ask user for a fruit to be deletedfrom list
fruitDeletion = raw_input('Pick a fruit to delete from the list:')
userRemoved = fruits[:]
userRemoved.remove(fruitDeletion)
print userRemoved

#  Ask user which fruits they like, print as list
userFruits = fruits[:]
for fruit in userFruits[:]:
    likeFruit = raw_input("Do you like " + fruit + "? ")
    if likeFruit == "no":
        userFruits.remove(fruit)
print userFruits

# Print orginal list and reversed version of original list
reverseFruits = fruits[:]
reverseFruits.reverse()

fruitsprint()
print reverseFruits
