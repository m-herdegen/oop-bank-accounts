# contains Account class and any future bank account logic

from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.all_accounts()

    #future bank logic
    def __str__(self):
        for account in self.accounts:
            print(account)
        return '* * * * * * * * * * * * * * * * *'

new_bank = Bank('super cool')
print(new_bank)