<<<<<<< HEAD
<<<<<<< HEAD

def cigar_party(cigars, weekend):
    """
    Return whether squirrl party is successful.
=======
def squirrel_party(cigars, weekend):
    """
    Return whether squirrel party is successful.
>>>>>>> b511bec3360be46e9dffa894cee2ea43fe693bfc
=======
def squirrel_party(cigars, weekend):
    """
    Return whether squirrel party is successful.
>>>>>>> task6

    Args:
        cigars (int): number of cigars smoked
        weekend (boolean): whether or not it is a weekend
<<<<<<< HEAD
<<<<<<< HEAD
    Return: 
        whether there were between 40 and 60 cigars inclusive if on a weekday,

    """
    if (not weekend) and ((cigars >= 40) and (cigars <= 60)):
        return True
    elif ()

    else:
        return False

if __name__ == '__main__':
    print(cigar_party(30, False))
    print(cigar_party(50, False))
    print(cigar_party(70, True))
=======
=======
>>>>>>> task6
    Return:
        whether there were between 40 and 60 cigars inclusive
        if on a weekday, and otherwise on weekends, you
        can't have enough cigars.
    """
    if (not weekend) and ((cigars >= 40) and (cigars <= 60)):
        return True
    else:
        return False

if __name__ == "main":
    if (squirrel_party(40, False)):
        print("Successful weekday party")
    else:
        print("It bombed.")

    if (squirrel_party(70, True)):
        print("Sky's the limit!")
    else:
        print("Sadface.")
<<<<<<< HEAD
>>>>>>> b511bec3360be46e9dffa894cee2ea43fe693bfc
=======
>>>>>>> task6
