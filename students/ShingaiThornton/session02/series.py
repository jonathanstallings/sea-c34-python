def fibonacci(n):

    """

      Calculate the nth number in a fibonacci sequence

      Args:
         n: the number in the sequence to return
      Returns: the nth number in the fibonacci sequence

   
    """

    A = 0
    B = 1
    Counter = 1
    C = 0
    
    while Counter <= n :
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            return C   

def lucas(n):
    """
        Calculate the nth number in a lucas sequence

        Args:
            n: the number in the sequence to return
        Returns: the nth number in the lucas sequence

    """
    
    A = 2
    B = 1
    Counter = 1
    C = 0   
    
    while Counter <= n:
        C = A + B
        A = B
        B = C
        Counter = Counter + 1
        if (Counter + 1) == n:
            return C

def sum_series(x, y  = 0, z = 1):
    """ 
        Calculate numbers in a series

        Args:
            x: Required paramater specifying number in the sequence to return
            y: Optional parameter specifying first number in a series
            z: Optional parameter specifying second number in a series

        Returns: The nth number in either a fibonacci or lucas sequence
    """
    if y == 2 and z == 1:
        return lucas(x)
    else:
        return fibonacci(x)

if __name__ == "__main__":
    #A statement to test that lucas(5) returns the 7, the value of the 5th number in the lucas sequence
    assert(lucas(5) == 7)
    
    #A statement testing that fibonacci(5) returns 3, the value of the 5th number in the fibonaci sequence
    assert(fibonacci(5) == 3)
    
   # A statement testing that sum_series function works properly for both lucas and fibonacci statments
    assert(sum_series(3,2,1) == 3)
    assert(sum_series(3, 0,1 ) == 1)