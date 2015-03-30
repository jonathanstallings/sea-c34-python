# How many times do you want to be reminded?
def reminder(times):
    """
    Prompt the user for an amount and prints that amount of reminders.

    Args:
        input1: the user's desired number of times to be reminded
    Return:
        prints the number of reminders the user wants
    """
    if times < 1:
        print "You said not to remind you."
    else:
        counter = 0
        while (counter < times):
            print("Do your homework!")
            counter += 1

input1 = raw_input("How many times reminders do you want? ")
reminder(int(input1))


# What's the sum of all the numbers on the list?

nums = [25, 29, 31, 41]


def find_sum(numbers):
    """
    Return the total sum of the numbers on the list.

    Args:
        nums: the list of numbers to be added
    Return:
        The total sum
    """
    total_sum = 0
    for i in nums:
        total_sum += i
    return total_sum

print find_sum(nums)


# Do you want to stop looping?

def loop():
    """
    Loop until user tells program to stop (enters 'N')

    Args:
        none
    Return:
        prints statement "Loop", "Huh?", or "Bye!"
    """
    while True:
        user_input = raw_input("Loop? (Y/N) ")
        if (user_input.upper() == "Y"):
            pass
        elif (user_input.upper() == "N"):
            print "Bye!"
            break
        else:
            print "Huh? Type \"Y\" or \"N\"."

loop()
