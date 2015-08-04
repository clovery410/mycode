def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    i = 0
    while lst[i] != start:
        i = i + 1

    new_lst = lst[:i+1] + lst[-1:i:-1]
    
    for j in range(len(lst)):
        lst[j] = new_lst[j]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
