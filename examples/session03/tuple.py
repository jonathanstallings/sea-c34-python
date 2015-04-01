def update_list_in_tuple(method='extend', new=['new', 'values']):
    """
    Check if tuple shows updated values of nested list.

    Args:
        method: the method to change list values.
        new: the new value(s) for the list.
    Returns:
        print out of test and result.

    """
    myList = ['old', 'values']
    myTuple = (0, 1, 2, myList)
    msg = u"myList is {myList}, and myTuple is {myTuple}.\n" \
        .format(myList=myList, myTuple=myTuple)
    if method == 'append':
        myList.append(new)
    elif method == 'extend':
        myList.extend(new)
    elif method == 'replace':
        myList = new
    else:
        print(u"Please use append, extend, or replace.")
        return
    msg += u"mList has been updated to {myList}.\n".format(myList=myList)
    msg += u"myList is now {myList}, and myTuple is {myTuple}.\n" \
        .format(myList=myList, myTuple=myTuple)
    print(msg)
    try:
        assert(myList == myTuple[3])
        print(u"The new values were updated in the tuple.")
    except:
        print(u"The new values did not update in the tuple.")


# update_list_in_tuple()
# result: value reassignment is not updated in tuple; modification is.
