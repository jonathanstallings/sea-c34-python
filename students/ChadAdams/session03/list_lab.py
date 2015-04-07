#!/usr/bin/env python
import StringIO

bowl = ['Apples', 'Pears', 'Oranges', 'Peaches']
print bowl

user_fruit = raw_input('Enter another fruit: ')
print user_fruit
bowl.append(user_fruit)
print bowl
user_num = raw_input('Enter a number between 1 and ' + str(len(bowl)) + ": ")
print "You've chosen " + bowl[int(user_num) -1]
bowl = ['Pineapple'] + bowl
print bowl
bowl.insert(0, 'Papaya')
print bowl
for x in bowl[:]:
    if x[0] == 'P':
        print x


bowl = ['Apples', 'Pears', 'Oranges', 'Peaches']
print bowl
bowl.pop(len(bowl)-1)
print bowl
user_del = raw_input('Enter a fruit to remove: ')
bowl.remove(user_del)
print bowl

bowl = ['Apples', 'Pears', 'Oranges', 'Peaches']
print bowl
bowl += bowl
print bowl
user_del2 = raw_input('Enter another fruit to remove: ')

for x in bowl[:]:
        if x == user_del2:
            bowl.remove(x)

print bowl


bowl = ['Apples', 'Pears', 'Oranges', 'Peaches']
print bowl

for x in bowl[:]:
    answer = raw_input('Do you like %s?: ' % x.lower())
    if answer.upper() == 'YES':
        continue
    elif answer.upper() == "NO":
        bowl.remove(x)
        continue
    while answer.upper() != 'YES' or answer.upper() != 'NO':
        answer = raw_input('Please respond with a yes or no. ')
        if answer.upper() == 'YES':
            break
        elif answer.upper() == "NO":
            bowl.remove(x)
            break

print bowl



bowl = ['Apples', 'Pears', 'Oranges', 'Peaches']
bowl_copy = []

for x in bowl[:]:
    count = len(bowl_copy)
    letters = tuple(bowl[count -1])
    wordcount = len(letters)
    backword = ''
    reverse = wordcount - 1
    for y in range(wordcount):
        backword += letters[reverse-y]

    bowl_copy.append(str(backword))

bowl.pop(len(bowl)-1)
print bowl
print bowl_copy
