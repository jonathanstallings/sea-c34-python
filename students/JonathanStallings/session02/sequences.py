from __future__ import print_function


def slice_overkill():
    """What happens when you try to slice beyond range of a list?"""
    my_list = []
    for x in range(10):
        my_list.append(x)
    else:
        msg = (u"my_list is {my_list}.\n".format(my_list=my_list))
    msg += (u"Deleting [3:50] from my_list!\n")
    del my_list[3:50]
    msg += (u"my_list is {my_list}.\n".format(my_list=my_list))
    print(msg)

# slice_overkill()
# result: No error. Python just slices to end of the list.


def slice_confusion():
    """What happens if you slice with odd start and end points?"""
    my_list = []
    for x in range(10):
        my_list.append(x)
    else:
        msg = (u"my_list is {my_list}.\n".format(my_list=my_list))
    msg += (u"Deleting [-5:4] from my_list!\n")
    del my_list[-5:4]
    msg += (u"my_list is {my_list}.\n".format(my_list=my_list))
    print(msg)

# slice_confusion()
# result: No error, but no deletion due to poor start and end points.


def update_list_in_tuple(method='extend', new=['new', 'values']):
    """
    Check if tuple shows updated values of nested list.

    Args:
        method: the method to change list values (append, extend, reassign)
        new: the new value(s) for the list.
    Returns:
        print out of test and result.

    """
    my_list = ['old', 'values']
    my_tuple = (0, 1, 2, my_list)
    msg = u"my_list is {my_list}\nmy_tuple is {my_tuple}.\n" \
        .format(my_list=my_list, my_tuple=my_tuple)
    print(msg)

    msg = u"Modifying my_list with "
    if method == 'append':
        msg += u"append.\n"
        my_list.append(new)
    elif method == 'extend':
        msg += u"extend.\n"
        my_list.extend(new)
    elif method == 'reassign':
        msg += u"reassignment.\n"
        my_list = new
    else:
        print(u"Please use append, extend, or reassign.")
        return

    msg += u"my_list has been updated to {my_list}.\n".format(my_list=my_list)
    msg += u"my_list is now {my_list}, and my_tuple is {my_tuple}.\n" \
        .format(my_list=my_list, my_tuple=my_tuple)
    print(msg)

    if (my_list == my_tuple[3]):
        print(u"The new values were updated in the tuple.\n")
    else:
        print(u"The new values did not update in the tuple.\n")


# update_list_in_tuple()
"""
result: Reassignment of my_list symbol breaks connection to value in tuple.
Other manipulations of the values directly are updated in the tuple.
On reflection, this seems obvious, but naively I thought the symbol my_list
was stored in the tuple, not its referrenced value.
"""
