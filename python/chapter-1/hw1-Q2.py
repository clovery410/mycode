from operator import sub
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return sub(sum_of_squares(a, b, c), pow(min(a, b, c), 2))

def sum_of_squares(a, b, c):
    return pow(a, 2) + pow(b, 2) + pow(c, 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
