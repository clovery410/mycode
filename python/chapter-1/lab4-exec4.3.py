def pair_star(phrase):
    """
    >>> pair_star("hiihhi")
    'hi*ih*hi'
    >>> pair_star("woodlands have squirrels")
    'wo*odlands have squir*rels'
    >>> pair_star("h")
    'h'
    """
    if len(phrase) <= 1:
        return phrase
    elif first(phrase) == second(phrase):
        return first(phrase) + '*' + second(phrase) + pair_star(rest(rest(phrase)))
    return first(phrase) + pair_star(rest(phrase))

def first(word):
    return word[0]

def second(word):
    return word[1]

def rest(word):
    return word[1:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
