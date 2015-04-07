def ack(m, n):

    '''This module performs the ackerman function on a pair of numbers.'''
    '''According to wikipedia, "the ackerman function is a total computable'''
    '''function that is not primitive recursive. All primitive recursive'''
    '''functions are total and computable, but the Ackermann function '''
    '''illustrates that not all total computable functions are primitive
    recursive.'''

    '''Numeric arguments:
    m : an integer
    n : an inetger
    Returns: an integer
    '''
    raise ValueError('number must be an integer')
    if m < 0:
        return None
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

    if __name__ == '__main__':
        # Test the range of n in ackerman function with m at zero
        print(ack(0, 0))
        print(ack(0, 1))
        print(ack(0, 2))
        print(ack(0, 3))
        print(ack(0, 4))
        # Test the range of n in ackerman function with m at one
        print(ack(1, 1))
        print(ack(1, 2))
        print(ack(1, 3))
        print(ack(1, 4))
        # Test the range of n in ackerman function with m at two
        print(ack(2, 1))
        print(ack(2, 2))
        print(ack(2, 3))
        print(ack(2, 4))
        # Test the range of n in ackerman function with m at three
        print(ack(3, 1))
        print(ack(3, 2))
        print(ack(3, 3))
        print(ack(3, 4))
        # All tests pass

        def test_math_functs():
            for i in range(3):
                if ack(i, (i + 1)):
                    print('All Tests Pass')
                else:
                    print('Tests failed')

        test_math_functs()
