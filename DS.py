# in This Module we define an api for the main.py
# methods in Core object must be able to do anything we need the backend do
# other classes, functions or constants can be defined for internal use.
from DSModels import Account, Manager, Employee, Customer
from dataclasses import dataclass
from random import randint

dict_error = {1: 'There is not enough money in your account',
              2: 'There is no such account number ',
              3: 'There is no such user '}


@dataclass
class Core:
    '''
    Core part of DS
    '''

    users = {'customers': {}, 'employees': {},
             'accounts': {}, 'branches': {}, 'admin': ''}

    def check_login(self, username: str, password: str, types: str):
        '''
        check_login(username=string,password=string,
        type=between (customers,empolyees,branches,admin))
        return object if True else return There is no such a user
        '''
        if username in self.users[types].keys() and (password == self.users[types][username].password):
            return self.users[types][username]
        else:
            return 3  # There is no such a user

    def create_account(self, username: str, amount=0):
        '''
        get username and return account number
        '''
        while True:
            account_number = randint(10**16, (10**17)-1)

            if account_number not in self.users['accounts'].keys():
                self.user['custumers'][username].add_account(account_number)
                self.user['accounts'][account_number] = Account(
                    balance=amount, account_number=account_number, owner=username)
                return account_number

    def deposit(self, account_number: int, amount: int):

        self.users['accounts'][account_number].deposit(amount)

    def get_balance(self, account_number):
        return self.user['accounts'][account_number].balance

    def withdraw(self, account_number, amount):
        return self.user['accounts'][account_number].withdraw(amount)

    def funds_transfer(self, account_number_send, account_number_get, amount):

        self.user['accounts'][account_number_send].fund_transfer(
            amount=amount, account_number_o=account_number_get, types='withdraw')
        self.user['accounts'][account_number_get].fund_transfer(
            amount=amount, account_number_o=account_number_send, types='deposit')

    def transfer_history(self, username, account_number):
        'return dict'
        pass

    def get_account_numbers(self, username):
        'return int'
        pass

    def all_accounts(self, username):
        'return accounts obj'
        pass

    def change_username(self, old_username, new_username):
        pass

    def change_password(self, username, old_password, new_password):
        pass

    def create_user(self, user_type):
        pass

    def search_user(self, username):
        pass

    def add_account(self, username):
        pass

    def del_account(self, username, account_number):
        pass

    def user_detail(self, username):
        pass

    def user_detail_change(self, username, **kwarg):
        pass

    def create_branch(self):
        pass

    def del_branch(self, branch_name):
        pass

    def get_branch_employees(self, branch_name):
        pass

    def get_all_employee(self):
        pass

    def get_all_customer(self):
        pass

    def get_all_user(self):
        pass

    def employees_payment(self):
        pass

    def account_fee(self):
        pass

    def transfer_fee(self, account_number):
        pass

    def get_bank_account_balance(self):
        pass

    def del_user(self, username, user_type):
        pass
