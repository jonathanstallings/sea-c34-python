def fibonacci(n):
    """
    Calculates the nth value of the fibonacci series

    Args: 
        n (int): the number of the series desired
    Returns:
        nth value of the fibonacci series starting at 0th value

    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n  - 1) + fibonacci(n - 2)

def lucas(n):
    """
    Calculates the asdfnth value of the lucas series

    Args: 
        n (int) : the number of the series desired
    Returns:
        nth value of the lucas series starting at 0th value

    """
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else: 
        return lucas(n  - 1) + lucas(n - 2)

def sum_series(n, first_value=0, second_value=1):
    """
    Calculates the nth value of the summation series

    Args: 
        n (int) : number of the series desired
        first_value (int) : first value element for the given series defaulting to 0
        second_value (int) : second element for the given series defaulting to 1
    Returns:
        nth value of the series startin with first_value and second_value 
        starting at 0th value

    """
    if n == 0:
        return first_value
    elif n == 1:
        return second_value
    else: 
        return sum_series(n  - 1, first_value, second_value) +\
        sum_series(n - 2,first_value, second_value)


# ******************** Test Code ************************** #
if __name__ == "__main__":
    # Testing Fibonacci Series 
    print("Testing Fibonacci series")
    for i in range (8):
        print (str(fibonacci(i)) + ", "),
    print("...")
    # Testing Lucas Series 
    print("Testing Lucas series")
    for i in range (8):
        print (str(lucas(i)) + ", "),
    print("...")
    # Testing Sum Series Function
    print("Testing Fibonacci Series using generic sum_series option")
    for i in range (8):
        print (str(sum_series(i)) + ", "),
    print("...")
    print("Testing Lucas Series using sum_series option with 3 arguments")
    for i in range (8):
        print (str(sum_series(i, 2, 1)) + ", "),
    print("...")
