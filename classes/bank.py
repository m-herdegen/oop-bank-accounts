# contains Account class and any future bank account logic

from classes.account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.all_accounts()

    #future bank logic
    def __str__(self):
        for account in self.accounts:
            print(account)
        return '* * * * * * * * * * * * * * * * *'

    def find(self):
        input_id = input('please enter an id to search by: ')
        return Account.find(int(input_id))
        


