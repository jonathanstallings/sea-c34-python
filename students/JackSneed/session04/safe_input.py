def safe_input(key):
    try:
        input_error = raw_input(key)
    except (EOFError, KeyboardInterrupt):
        input_error = None
    return input_error

safe_input()
