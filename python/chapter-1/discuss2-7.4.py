from operator import add
def identity(x):
    return x

def lazy_accumulate(f, start, n, term):
    """
    Takes the same arguments as accumulate from next week's homework and returns a function that takes a second integer m and will return the result of accumulating the first n numbers starting at 1 using f and combining that with the next m integers.

    Arguments:
    f - the funtion for the first set of numbers.
    start - the value to combine with the first vaule in the sequence.
    n - the stopping point for the first set of numbers.
    term - function to be applied to each number before combining.

    Returns:
    A function (call it h) h(m) where m is the number of additional vaules to combine.

    >>> # The following does
    >>> # (1 + 2 + 3 + 4 + 5) + (6 + 7 + 8 + 9 + 10)
    >>> lazy_accumulate(add, 0, 5, identity)(5)
    55
    """
    def second_accumulate(m):
        return accumulate(f, start, n + m, term)
    return second_accumulate

def accumulate(combiner, start, n, term):
    curr, accu = start, term(start)
    while curr < n:
        curr = curr + 1
        accu = combiner(term(curr), accu)
    return accu


if __name__ == "__main__":
    import doctest
    doctest.testmod()
