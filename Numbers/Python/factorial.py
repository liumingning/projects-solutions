'''
Factorial Finder - The Factorial of a positive integer, n, is defined as the
product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0,
is defined as being 1. Solve this using both loops and recursion.
'''


def fact_with_recursion(n):
    '''
    >>> fact_with_recursion(5)
    120
    '''
    return fact_with_recursion(n - 1) * n if n > 1 else 1

def fact_with_loops(n):
    '''
    >>> fact_with_loops(5)
    120
    '''
    result = 1
    for x in range(1, n+1):
        result *=x
    return result
