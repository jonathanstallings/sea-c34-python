# 2 Questions
def caught_break():
    """Will a bald except statement prevent ctrl-c?"""
    while True:
        try:
            reply = raw_input(u'Type q and enter to end\n')
            if reply == 'q':
                break
            else:
                continue
        except:
            continue


# caught_break()
# result: The exceptino catches the break signal. Nasty!

def caught_raise():
    """Will a bald except statemnt catch a raise statement?"""
    try:
        raise TypeError
    except:
        print('Prevented raised exception')


# caught_raise()
# result: The except statement caught the TypeError as normal.
