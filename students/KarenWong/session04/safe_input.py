def safe_input(input):
    try:
        return raw_input(input)
    except (EOFError, KeyboardInterrupt):
        return None
        
        
safe_input("Hello")
