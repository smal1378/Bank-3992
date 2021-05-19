# in This Module we define an api for the main.py
# methods in Core object must be able to do anything we need the backend do
# other classes, functions or constants can be defined for internal use.

class Core:
    def __init__(self):
        self.users = {'customers': {}, 'employees': {},
                      'accounts': {}, 'branches': {}, 'admin': ''}

    def check_login(self, username, password):
        pass

    def create_account(self, username):
        'return account_number'

    def deposit(self, account_number, amount):
        pass

    def get_balance(self, username, account_number):
        pass

    def withdraw(self, username, account_number, amount):
        pass

    def funds_transfer(self, username, account_number_1, account_number_2, amount):
        pass

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
