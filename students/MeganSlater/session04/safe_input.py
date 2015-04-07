def safe_input(x):
    try:
        raw_input(x)
    except (EOFError, KeyboardInterrupt):
        return "None"
safe_input("What is your favorite color? ")
