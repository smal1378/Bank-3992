# in This Module we define an api for the main.py
# methods in Core object must be able to do anything we need the backend do
# other classes, functions or constants can be defined for internal use.
from DSModels import Account, Manager, Employee, Customer
from dataclasses import dataclass
from random import randint

dict_error = {1: 'There is not enough money in your account',
              2: 'There is no such account number ',
              3: 'There is no such user ',
              4: 'The username is already exist',
              5: 'Password is wrong'}


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
        if username in self.users[types].keys() and (
                password == self.users[types][username].password):
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

    def account_history(self, account_number, types=None):
        '''
        transfer_history(account_number=integer,types=(withdraw,deposit,fund_transfer))
        '''
        if types == None:
            return self.users['accounts'][account_number].history.values()
        else:
            return self.users['accounts'][account_number].history[types]

    def customer_history(self, username: str):
        return self.users['customers'][username].history.values()

    def get_account_numbers(self, username: str):
        ''' return list of accounts number'''

        return self.users['customers'][username].accounts

    def all_accounts(self, username: str):
        '''return accounts obj'''
        accounts = self.get_account_numbers(username)
        return (self.users['accounts'][i] for i in accounts)

    def change_username(self, old_username, new_username, types):
        '''
        change_username(old_username=string,new_username=string,types=(customers,branches,employees))
        '''
        if new_username in self.users[types].keys():
            return 4  # username is already exist
        else:
            self.users[types][new_username] = self.users[types][old_username]
            del self.users[types][old_username]

    def change_password(self, username: str, old_password: str, new_password: str, types):
        '''
        change_password(username=string,old_paasword=string,new_password=str,types=(customers,branches,employees))
        '''

        if old_password == self.users[types][username].password:
            self.users[types][username].password = new_password
        else:
            return 5  # password is wrong

    def search_user(self, username):
        '''return an object if exist else return 3'''
        for i in self.users.keys():
            for j in i:
                if username == self.users[i][j].username:
                    return self.users[i][j]
        return 3  # there is not such a user

    def del_account(self, username: str, account_number: int):
        del self.users['accounts'][account_number]
        self.users['customers'][username].accounts.remove(account_number)

    def user_detail(self, username):
        'return list of methods if exists else return 3'
        user = search_user(username)
        if user == 3:
            return 3  # there is no such a user
        else:
            return

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
