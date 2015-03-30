# Is your name on the list?

def check_list(name):
    """
    Print whether name is or is not on the roster.

    Args:
        string: name of person to be checked
    Return:
        prints result if person is on the list or not.
    """
    roster = [u"Earl", u"Russell", u"Richard", u"Kam", u"Bruce"]
    roster_check = name in roster
    if roster_check is True:
        print("Yes, %s, you're on the roster." % name)
    else:
        print("No, %s, you're not on the roster." % name)

check_list(u"Earl")

# Would you like to edit your workout?

def edit_workout():
    """
    Print workout list and asks if user would like to add another workout.

    Args:
        none
    Return:
        prints new workout or ok statement
    """
    workout = ["Bench Press", "Shoulder Press", "Dips", "Cable Cross"]
    print workout
    resp = raw_input("Would you like to add to your workout? (Y/N) ")
    if (resp.lower() == "y"):
        exercise = raw_input("Enter the exercise you'd like to add: ")
        workout.append(exercise)
        print "Here is your workout: "
        print workout
    elif (resp.lower() == "n"):
        print "Ok, Git-R-Done!"
    else:
        print "Sorry, you must enter \"Y\" or \"N\"."
        edit_workout()

edit_workout()

# Creating a username

def check_username_length(name):
    """
    Checks if created username length is 8+ characters.

    Args:
        string: user's desired username
    Return:
        prints statement approving or disapproving user's username.
    """
    name_len = len(name)
    if name_len < 8:
        print("%s is %i characters. It must be 8 or more." % (name, name_len))
    else:
        print("Your username is %s." % name)

check_username_length("codemonkey12")
