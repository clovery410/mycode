class Amount(object):
    """An amount of nickels and pennies.

    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value
    22
    >>> a.nickels = 5
    >>> a.value
    32
    """
    def __init__(self, nickels, pennies):
        self.nickels = nickels
        self.pennies = pennies
        
    @property
    def value(self):
        return (self.nickels * 5 + self.pennies)

class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than four pennies, by converting excess pennies to nickels.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels
    4
    >>> a.pennies
    2
    >>> a.value
    22
    """
    def __init__(self, nickels, pennies):
        while pennies > 4:
            nickels = nickels + 1
            pennies = pennies - 5
        self.nickels = nickels
        self.pennies = pennies
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
