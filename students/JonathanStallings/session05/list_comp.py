def count_evens(nums):
    """
    Return the number of even ints in the given array.

    Args:
        nums: the array of numbers to check

    Returns: the number of even ints
    """
    evens_list = [x for x in nums if (x % 2 == 0)]
    return len(evens_list)


assert(count_evens([2, 1, 2, 3, 4]) == 3)
assert(count_evens([2, 2, 0]) == 3)
assert(count_evens([1, 3, 5]) == 0)

