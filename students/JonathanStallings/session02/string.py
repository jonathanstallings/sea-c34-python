from __future__ import print_function
import sys
import traceback


def highest_ordinal():
    """Which letter has the highest ordinal value?"""
    string = u"The quick brown fox leaped!"
    msg = u"The max was {maxOrd} and its value was {maxValue}." \
        .format(maxOrd=max(string), maxValue=ord(max(string)))
    print(msg)

# highest_ordinal()
# result: The max was x and its value was 120.


def lowercase_number():
    """What happens when you try to lowercase a number?"""
    num = 16
    try:
        print(num.lower())
    except:
        print(u"Use of lowercase method on number raises exception.")
        traceback.print_exc(file=sys.stdout)

# lowercase_number()
# result: Using a lowercase (string) method on number throws an AttributeError.


def input_type():
    """Does raw_input always return a string?"""
    user_input = raw_input()
    print(type(user_input))


# input_type()
# result: Yes. raw_input always returns a string.
