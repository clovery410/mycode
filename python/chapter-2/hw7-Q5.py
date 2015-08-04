class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> john = Account('John')
    >>> jack = Account('Jack')
    >>> john.deposit(10)
    10
    >>> john.deposit(5)
    15
    >>> john.interest
    0.02
    >>> jack.deposit(7)
    7
    >>> jack.deposit(5)
    12
    """
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class SecureAccount(Account):
    def __init__(self, account_holder, password):
        self.holder = account_holder
        self.password = password
        self.count = 0
        self.balance = 0

    def withdraw(self, amount):
        return 'This account requires a password to withdraw'

    def secure_withdraw(self, amount, pw_input):
        if self.count >= 3:
            return 'This account is locked'
        elif pw_input != self.password:
            self.count += 1
            return 'Incorrect password'
        else:
            return Account.withdraw(self, amount)


class MoreSecureAccount(Account):
    def __init__(self, account_holder, password):

        def function():
            attribute = {'get_password': password, 'counter': 0}
            
            def compare_value(value):
                if attribute['get_password'] != value:
                    attribute['counter'] = attribute['counter'] + 1
                    return False
                return True
                
            def get_counter():
                return attribute['counter']

            dispatch = {'get': get_counter, 'compare': compare_value}
            return dispatch

        self.config = function()            
        self.holder = account_holder
        self.balance = 0

    def withdraw(self, amount):
        return 'This account requires a password to withdraw'

    def secure_withdraw(self, amount, pw_input):
        
        if self.config['get']() >= 3:
            return 'This account is locked'
        elif not self.config['compare'](pw_input):
            return 'Incorrect password'
        else:
            return Account.withdraw(self, amount)



import unittest

class SecureAccountTest(unittest.TestCase):
    """Test the secureAccount class."""
    def setUp(self):
        self.account = SecureAccount('Alyssa P. Hacker', 'p4ssw0rd')

    def test_secure(self):
        acc = self.account
        acc.deposit(1000)
        self.assertEqual(acc.balance, 1000, 'Bank error! Incorrect balance')
        self.assertEqual(acc.withdraw(100), 'This account requires a password to withdraw')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'), 900, "didn't withdraw 100")
        self.assertEqual(acc.secure_withdraw(100, 'h4x0r'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, 'n00b'), 'Incorrect password')
        self.assertEqual(acc.secure_withdraw(100, '1337'), 'Incorrect password')
        self.assertEqual(acc.balance, 900, 'Withdrew with bad password')
        self.assertEqual(acc.secure_withdraw(100, 'p4ssw0rd'), 'This account is locked')
        self.assertEqual(acc.balance, 900, 'Withdrew from locked account')


class MoreSecureAccountTest(SecureAccountTest):
    """Test the MoreSecureAccount class."""
    def setUp(self):
        self.account = MoreSecureAccount('Alyssa P. Hacker', 'p4ssw0rd')


if __name__ == "__main__":
    hack = MoreSecureAccount('Alyssa P. Hacker', 'p4ssw0rd')
    hack.deposit(1000)
    print(hack.secure_withdraw(100, '1227'))
    
    print(hack.secure_withdraw(100, '22222'))

    print(hack.secure_withdraw(100, '127'))
    
    print(hack.secure_withdraw(100, '2222'))
    print(hack.secure_withdraw(100, '22222'))

    print(hack.secure_withdraw(100, '127'))
    
    print(hack.secure_withdraw(100, '2222'))

    #print(hack.config['get']('get_password'))
    unittest.main()
