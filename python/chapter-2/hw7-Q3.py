from vending import VendingMachine

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please.'
    >>> m.ask('please give up a teaspoon')
    'Thanks for asking, but I know not how to give up a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    def __init__(self, instance):
        self.instance = instance
        

    def ask(self, message, *args):
        if 'please' in message:
            if hasattr(self.instance, message[7:]):
                method = getattr(self.instance, message[7:])
                return method(*args)
            else:
                return 'Thanks for asking, but I know not how to' + message[6:]
        else:
            return 'You must learn to say please.'
            
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
