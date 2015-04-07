def safe_input(user_prompt):
    """
    This wrapper function takes in a string that is to be prompted
    to the user. If an EOFError or KeyboardInterrupt error is raised,
    the function returns None.
    Args:
        user_prompt: This is the question to be prompted to the user.
    Result:
        return string (user's input) or None

    """
    try:
        user_input = raw_input(user_prompt)
        return user_input
    except (EOFError, KeyboardInterrupt):
        return None

# example of function being called
safe_input("Type your input: ")
