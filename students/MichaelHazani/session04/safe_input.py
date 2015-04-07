def safe_input():
    try:
        input = raw_input(">")

    except (EOFError, KeyboardInterrupt):
        return 'None'
        # now do things with input, of course.

safe_input()
