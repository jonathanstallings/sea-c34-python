# Example: NameError
def name_error(x, y):
    return x + z

print name_error(1, 2)

# Example: TypeError

def type_error(x, y):
    total = x + y
    return total

type_error(1, "Joe")


# Example: SyntaxError


def synatx_error(value):
    if value > 0:
        print(u"The number is positive")
    else
        print(u"The number is negative")

synatx_error(12)

# Example: AttributeError

person = "Joe"


def attribute_error():
    return person.age

attribute_error()
