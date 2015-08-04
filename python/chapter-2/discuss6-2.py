def replace_all(d, x, y):
    """Replaces all values of x with y.
    >>> d = {1: {2: 3, 3: 4}, 2: {4: 4, 5: 3}}
    >>> replace_all(d, 3, 1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """
    for k in d.keys():
        if type(d[k]) == dict:
            replace_all(d[k], x, y)
        elif d[k] == x:
            d[k] = y

def rm(d, x):
    """Removes all pairs with value x.
    >>> d = {1: 2, 2: 3, 3: 2, 4: 3}
    >>> rm(d, 2)
    >>> d
    {2: 3, 4: 3}
    """
    for k in d.keys():
        if d[k] == x:
            del d[k]
            return rm(d, x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
