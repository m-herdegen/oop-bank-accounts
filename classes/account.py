# 2. Create an `Account` class which should have the following functionality:
#   - A new account should be created with an `ID` and an initial `balance`
#   - Should have a `withdraw` method that accepts a single parameter which represents the amount of money that will be withdrawn. This method should return the updated account balance.
#   - Should have a `deposit` method that accepts a single parameter which represents the amount of money that will be deposited. This method should return the updated account balance.
#   - Should be able to access the current `balance` of an account at any time.

#from owner import Owner
# from bank import Bank
import csv

class Account:

    def __init__(self, id, balance, open_date):
        #self.owner = Owner()
        self.id = id
        self.open_date = open_date
        if balance >= 0:
            self.balance = balance 
        else:
            raise Exception('You cannot create an account with a negative balance')

    @classmethod
    def all_accounts(cls):
        file_name = '../support/accounts.csv'
        account_list = []
        headings = ['id','balance','open_date']

        with open(file_name, newline='') as account_file:
            reader = csv.DictReader(account_file)
            reader.fieldnames = headings

            for row in reader:
                account_list.append(Account(row['id'],int(row['balance']),row['open_date']))
            
            # print(account_list)

        return account_list

    # def find(self, id):
    #     check = next((item for item in Bank.accounts if item.id == id), 'there is no account with that id')
    #     return check

    # withdraws money, returns account balance
    def withdraw(self, withdrawal_amt):
        
        if self.balance >= withdrawal_amt:
            self.balance -= withdrawal_amt

        else:
            raise Exception('You do not have enough money for this transaction')

        return self.balance

    # deposist money, returns account balance
    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account ID: {self.id}\nAccount balance: {self.balance}"
