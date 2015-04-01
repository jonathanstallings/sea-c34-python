#############################################
# This is for Task 4- Mathematical Series
############################################

'''
Fibonacci Series
0, 1, 1, 2, 3, 5, 8, 13, ...
The function for a Fibonnaci series is F(n) = F(n-1) + F(n-2)
Where n is the nth number in the series.
What we know- F(0) = 0, F(1) = 1, F(2) = 1
For this assignment, we calculate the nth number in the series
'''

def fibonacci(n):
        if n < 0:
                return None
        elif n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)

'''
Lucas Series
2, 1, 3, 4, 7, 11, 18, 29, ...
The function for the Lucas number is the same as Fibonacci,
except that the first number is a 2 instead of the 0,1 pair. 
For this assignment, we calculate the nth number in the series
'''

def lucas(n):
        if n < 0:
                return None
        elif n == 0:
                return 2
        elif n == 1:
                return 1
        else:
                return lucas(n-1) + lucas (n-2)


'''
Sum Series
Need- One required (user) and two optional parameters
The required parameter will determine which element in the series to print. 
The two optional parameters will have default values of 0 and 1 and will 
determine the first two values for the series to be produced.
To deal with this, make two variables - y = 0, z = 1
'''

def sum_series (n, y = 0, z = 1):
        if n < 0:
                return None
        elif n == 0:
                return y #0!
        elif n == 1:
                return z #1!
        else:
                return sum_series(n-1,y,z) + sum_series(n-2,y,z)




'''
Testing
'''
if __name__ == "__main__":

        #After some testing- the assert command will not print out anything 
        # if the assertion is true.

        #Testing the Fibonacci Equation

        assert fibonacci(-1) == None
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

        # All of these passed. When I used assert fibonacci(1) = 4 as a test
        # (Obviously wrong!), an AssertionError was raised. 


        #Testing the Lucas Equation
        assert lucas(-14) == None
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(6) == 18

        # All passed!

        
        #Testing the series
        '''
        If we call this function with no optional parameters (y and z are 0 and 1, respectively),
        the fibonacci series should be produced. For example: 
        sum_series(4) should be equal to fibonacci(4)

        If we call the function with optional paramaters (in this case y and z are 2 and 1, respectively),
        the lucas series should be produced. For example:
        sum_series(4,2,1) should be equal to lucas(4)

        Pretty sure these can be done in a loop to save typing time
        '''

        #Fib and Sum_Series
        # y and z are still equal to 0 and 1, respectively in this case

        for n in range(11):
                #0 - 10
                assert sum_series(n) == fibonacci(n)


        # Lucas and Sum_Series
        # y and z need to be set to 2 and 1, respectively
        
        for n in range(11):
                assert sum_series(n,2,1) == lucas(n)


        print "All tests passed!"
