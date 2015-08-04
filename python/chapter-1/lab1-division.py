def factors(n):
    """Define a function factors(n) which takes in a numner, n, and prints out all the numbers that divide n evenly. 

    >>> factors(20)  #For example, a call with n=20 should result as follows(order doesn't matter):
    20
    10
    5
    4
    2
    1
    """
    i = n # The initial factor i = n
    while i > 0:
        if n % i == 0:
            print(i)
        i = i - 1
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()
