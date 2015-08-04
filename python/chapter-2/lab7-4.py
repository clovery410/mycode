class Account(object):
    """A bank account that allows deposits and withdrawls."""
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions.append(('withdraw', amount))
        return self.balance

class Check(object):
    def __init__(self, payable_to, amount):
        self.payable_to = payable_to
        self.amount = amount
        self.deposited = False


class CheckingAccount(Account, Check):
    """A bank account that charges for withdrawls."""
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        if self.holder != check.payable_to or check.deposited:
            print("The police have been notified.")
        else:
            self.deposit(check.amount)
            check.deposited = True


    
if __name__ == "__main__":
    eric_account = Account("Eric")
    eric_account.deposit(1000000)
    print(eric_account.transactions)
    eric_account.withdraw(100)
    print(eric_account.transactions)

    clover_account = CheckingAccount("Clover")
    clover_account.deposit(10000)
    print(clover_account.transactions)
    clover_account.withdraw(50)
    print(clover_account.transactions)

    check = Check("Steven", 42)
    steven_account = CheckingAccount("Steven")
    eric_account = CheckingAccount("Eric")
    eric_account.deposit_check(check)
    print(eric_account.balance)
    print(check.deposited)
    print(steven_account.balance)
    steven_account.deposit_check(check)
    print(check.deposited)
    steven_account.deposit_check(check)
    
