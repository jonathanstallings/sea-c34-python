import string
import codecs  # Use for validation testing

user = str(raw_input("Message to encrypt: "))
chars = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


def rot13(user):
    """Accept user input and translate each character to its respective
    character at 13 characters away.

        arg:
            user: User input taken from command line prompt.
        return:
            message: Output encrypted message using ROT13 translation."""
    message = string.translate(user, chars)
    print(message)


if __name__ == "__main__":
    assert(rot13(user) == codecs.encode(user, "rot_13"))
