#!/usr/bin/env python

def action_one ():
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit_list)
    
    user_fruit = raw_input("Please submit a new fruit to the list: ")
    print("You submitted %s" %user_fruit)
    fruit_list.append(user_fruit)

    user_number = raw_input("Please select a fruit from the list using a numeral: ")
    user_number = int(user_number)
    print("You selsected the number %d which corresponds to  the fruit %s"\
     % (user_number, fruit_list[user_number - 1]))
    
    fruit_list  = ["Apricots"] + fruit_list
    fruit_list.insert(0, "Strawberries")

    print("Here are the fruits that begin with 'P':")
    for fruit in fruit_list:
        if fruit[0] == 'P':
            print(fruit)

    return fruit_list

def action_two(my_fruit_list):
    print(my_fruit_list)
    my_fruit_list.pop()
    print(my_fruit_list)


    my_fruit_list *= 2
    remove_fruit = raw_input("Please select a fruit you would like to remove from the list: ")
    
    while not(remove_fruit in my_fruit_list):
        print("That fruit is not in the list")
        remove_fruit = raw_input("Please select a fruit you would like to remove from the list: ")

    while remove_fruit in my_fruit_list:
            my_fruit_list.pop(my_fruit_list.index(remove_fruit))

    print(my_fruit_list)
    return my_fruit_list

def action_three(my_fruit_list):
    index = 0
   
    while index < len(my_fruit_list):
        answer = raw_input("Do you like %s  (yes/no): " %my_fruit_list[index].lower())
       
        while (answer != 'yes') & (answer != 'no'):
            answer = raw_input("That is not a valid answer. Please enter 'yes' or 'no':")
       
        if answer == 'no':
            my_fruit_list.pop(index)

        index += 1
    
    print(my_fruit_list)

def action_four(my_fruit_list):
     copy_list = list(my_fruit_list)
     for fruit in copy_list:
        copy_list[copy_list.index(fruit)] = fruit[::-1]

     my_fruit_list.pop()
     print ("This is the original list: ")
     print (my_fruit_list)
     print ("This is the copy list: ")
     print(copy_list)

#********************* TEST CODE ************************#
if __name__ == '__main__':
   this_list = tuple(action_one())
   action_two(list(this_list))
   action_three(list(this_list))
   action_four(list(this_list))
