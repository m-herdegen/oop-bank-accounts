from argparse import ArgumentError
from classes.account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
        if self.balance < 1000:
            raise ArgumentError
        
    def withdraw(self, withdrawal_amt):
        if self.balance - withdrawal_amt + 200 < 1000:
            self.balance -= withdrawal_amt + 200
        else:
            print('You do not have enough money for this transaction, so it was cancelled.')
        return self.balance

    def add_interest(self, rate):
        self.balance = self.balance * rate/100