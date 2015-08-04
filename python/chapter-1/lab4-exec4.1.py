def count_hi(phrase):
    """
    >>> count_hi("hihihihi")
    4
    >>> count_hi("hhjfdkfj")
    0
    >>> count_hi("")
    0
    >>> count_hi("hih")
    1
    """
    if len(phrase) <= 1:
        return 0
    elif first(phrase) == 'h' and second(phrase) == 'i':
        return count_hi(rest(rest(phrase))) + 1
    else:
        return count_hi(rest(phrase))

def first(word):
    return word[0]
    
def second(word):
    return word[1]

def rest(word):
    return word[1:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
