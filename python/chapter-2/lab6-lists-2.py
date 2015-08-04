def make_deck():
    """Now write a list comprehension that will create a deck of cards. Each element in the list will be a card, which is represented by a tuple containing the suit as a string and the value as an int.
    """
    return [(suit, value) for suit in ('heart', 'diamond', 'spade', 'club') for value in range(1, 14)]

print (make_deck())

