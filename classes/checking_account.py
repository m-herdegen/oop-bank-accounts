from classes.account import Account

class CheckingAccount(Account):

    def __init__(self, id, balance, open_date, num_checks_used):
        Account.__init__(self, id, balance, open_date)
        self.num_checks_used = 0

    def withdraw(self, withdrawal_amt):
        if self.balance - withdrawal_amt + 100 < 0:
            self.balance -= withdrawal_amt + 100
        else:
            print('You do not have enough money for this transaction, so it was cancelled.')
        return self.balance

    def withdraw_using_check(self, amount):
        if self.num_checks_used >= 3:
            amount += 2
        self.num_checks_used += 1
        if self.balance - amount < -1000:
            self.balance -= amount
        else:
            print('You do not have enough money for this transaction, so it was cancelled.')
        return self.balance 

    def reset_checks(self):
        self.num_checks_used = 0