class VendingMachine(object):
    """A vending machine that vends some product for some price.
    
    >>> v = VendingMachine('crab', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current crab stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your crab and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your crab.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.quantity = 0

    def vend(self):
        if self.quantity == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            difference = self.price - self.balance
            return 'You must deposit $' + str(difference) + ' more.'
        elif self.balance == self.price:
            self.balance = 0
            self.quantity = self.quantity - 1
            return 'Here is your ' + str(self.product) + '.'
        elif self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.quantity = self.quantity - 1
            return 'Here is your ' + str(self.product) + ' and $' + str(change) + ' change.'

    def restock(self, num):
        self.quantity = self.quantity + num
        return 'Current ' + str(self.product) + ' stock: ' + str(self.quantity)

    def deposit(self, money):
        self.balance = self.balance + money
        if self.quantity == 0:
            change = self.balance
            self.balance = self.balance - change
            return 'Machine is out of stock. Here is your $' + str(change) + '.'
        else:
            return 'Current balance: $' + str(self.balance)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
