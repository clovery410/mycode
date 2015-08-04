#1.1 Print out a countdown using recursion.
def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

#1.2 Change countdown to countup instead.
def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    if n <= 0:
        return
    countup(n - 1)
    print(n)    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
