def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    
    def withdraw(amount):
        nonlocal balance
        
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


wd = make_withdraw(20)
print(wd(5))
print(wd(3))
