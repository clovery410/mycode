class Account(object):
    """A bank account that has a non-negative balance."""
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


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1

tom_account = Account('Tom')
jim_account = Account('Jim')
Account.interest = 0.04
jim_account.interest = 0.08
print(tom_account.deposit(100))
print(tom_account.withdraw(90))
print(tom_account.interest)
print(jim_account.interest)
Account.interest = 0.05
print(tom_account.interest)
print(jim_account.interest)
checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)

such_a_deal = AsSeenOnTVAccount("John")
print(such_a_deal.balance)
print(such_a_deal.deposit(20))
print(such_a_deal.withdraw(5))
print(such_a_deal.deposit_charge)
print(such_a_deal.withdraw_charge)

print([c.__name__ for c in AsSeenOnTVAccount.mro()])
