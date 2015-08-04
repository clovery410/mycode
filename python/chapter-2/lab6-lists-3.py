def sort_deck(deck):
    deck.sort(key=lambda card: card[1])
    deck.sort(key=lambda card: card[0])
    return deck

deck = [('heart', 3), ('club', 1), ('heart', 2), ('spade', 9), ('diamond', 8), ('spade', 6)]

print(sort_deck(deck))
