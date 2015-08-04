def reverse(lst):
    """Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    
    for i in range(1, len(lst)):
        j = len(lst) -1 - i
        lst.append(lst[j])
        lst.remove(lst[j])

def rotate(lst, k):
    """Return a new list, with the same elements of lst, rotated to the right k.
    >>> x = [1, 2, 3, 4, 5]
    >>> rotate(x, 3)
    [3, 4, 5, 1, 2]
    """
    for el in lst:
        if el == k:
            i = lst.index(el)
    return lst[i:] + lst[:i]
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()
