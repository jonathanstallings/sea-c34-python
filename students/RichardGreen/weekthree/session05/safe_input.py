
'''The raw_input() function can generate two exceptions: - EOFError or
end-of-file (EOF) - KeyboardInterrupt or canceled input. - Create a wrapper
function, perhaps safe_input() that returns None rather than raising these
exceptions.'''


def safe_input():

    print "Enter a number:"

    input = raw_input()
    print "Your input:"
    print input

    try:
        input = int(input)
        # break
    except (KeyboardInterrupt, TypeError, ValueError, EOFError):
        None
        print(u"Input must be an integer, try again.")

if __name__ == "__main__":
    #
    safe_input()
