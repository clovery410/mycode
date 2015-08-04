def chicken(argument, generations=0):
    """ Argue whether or not the chicken came first.
    >>> chicken(True)
    "Chickens lay eggs!"
    >>> chicken(False) # is equivalent to egg(True)
    "Eggs hatch chickens! And they're cuter."
    >>> chicken(False, 1) # is equivalent to egg(True, 0)
    "Eggs hatch chickens! And they're cuter."
    """
    if generations <= 0:
        if argument:
            return "Chickens lay eggs!"
        return egg(not argument, generations)
    return egg(not argument, generations - 1)

def egg(argument, generations=0):
    """ Argue whether or not the egg came first."""
    if generations <= 0:
        if argument:
            return "Eggs hatch chickens! And they're cuter."
        return chicken(not argument, generstions)
    return chicken(not argument, generations - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

result = chicken(False, 1)
