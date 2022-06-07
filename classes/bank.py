# contains Account class and any future bank account logic

from classes.account import Account
from classes.owner import Owner

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = Account.all_accounts()
        self.owners = Owner.all_owners()

    #future bank logic
    def __str__(self):
        for owner in self.owners:
            print(owner)
        return '* * * * * * * * * * * * * * * * *'

    def find(self):
        input_id = input('please enter an id to search by: ')
        return Account.find(int(input_id))
        


