"""
in This Module we define an api for the main.py
methods in Core object must be able to do anything we need the backend do
other classes, functions or constants can be defined for internal use.
"""
from DSModels import Account, Customer, Branch, Employee, Manager
from dataclasses import dataclass
from random import randint

dict_error = {1: 'There is not enough money in your account',
              2: 'There is no such a account number ',
              3: 'There is no such a username ',
              4: 'The username is already exist',
              5: 'Password is wrong',
              6: 'There is no such a branch',
              7: 'number is smaller or equal to 0'}


@dataclass
class Core:
    '''
    Core part of DS
    '''

    users = {'customers': {},
             'employees': {},
             'accounts': {},
             'branches': {},
             'admin': '',
             'managers': {}}
# ============================admin part=================================

    def set_admin(self, username: str, password: str):
        '''set_admin also can be used for change password or username'''
        self.users['admin'] = {'username': username, 'password': password}

# ===========================global part=================================

    def check_login(self, username: str, password: str, types: str):
        '''
        check_login(username=string,password=string,
        type=between (customers,empolyees,managers,admin))
        return object if True else return 3 (There is no such a username)
        '''
        if types == 'admin':
            if self.users['admin'][username] == username and (
                    self.users['admin'][password] == password):
                return True
        elif username in self.users[types] and (
                password == self.users[types][username].password):
            return self.users[types][username]
        return 3  # There is no such a username

    def change_username(self, old_username, new_username, types):
        '''
        change_username(old_username=string,new_username=string,types=(customers,branches,employees,managers))
        '''
        if new_username in self.users[types]:
            return 4  # username is already exist
        self.users[types][new_username] = self.users[types][old_username]
        del self.users[types][old_username]

    def change_password(self, username: str, old_password: str,
                        new_password: str, types):
        '''
        change_password(username=string,old_paasword=string,new_password=str,
        types=(customers,branches,employees,managers))
        '''

        if old_password == self.users[types][username].password:
            self.users[types][username].password = new_password
        else:
            return 5  # password is wrong

    def search_user(self, username: str, types=None):
        '''
        search_user(username=string,types=(customers,branches,employees,managers))
        return an object if exist else return 3 '''
        if types in self.users:
            if username in self.users[types]:
                return self.users[types][username]
        else:
            for i in self.users:
                for j in i:
                    if username == self.users[i][j].username:
                        return self.users[i][j]
            return 3  # there is no such a username

    def user_detail_change(self, username, **kwargs):
        '''
        User(first_name=string,last_name=string,ID=string,address=string)
        Manager(salary=integer)
        employee(salary=integer)
        '''
        user = self.search_user(username)
        if user == 3:
            return 3  # there is no such a username
        attributes = vars(user)  # all methods of user
        for key, value in kwargs.items():
            if key in attributes:
                user.key = value

# ==========================account part================================

    def create_account(self, username: str, amount=0):
        '''
        create_account(self,username=string and must be in users[customers],
        amount=default 0)
        get username and return integer(account_number)
        '''
        if username not in self.users['customers']:
            return 3  # There is no such a username
        while True:
            account_number = randint(10**16, (10**17)-1)

            if account_number not in self.users['accounts']:
                # add to accounts attribute in customer class
                self.users['custumers'][username].add_account(account_number)
                # save account object in users[accounts]
                self.users['accounts'][account_number] = Account(
                    balance=amount, account_number=account_number,
                    owner=username)
                return account_number

    def deposit(self, account_number: int, amount: int):

        self.users['accounts'][account_number].deposit(amount)

    def get_balance(self, account_number):
        if account_number in self.users['accounts']:
            return self.users['accounts'][account_number].show_balance()
        return 2  # there is no such a account_number

    def withdraw(self, account_number: int, amount: int):
        return self.users['accounts'][account_number].withdraw(amount)

    def funds_transfer(self, account_number_send: int,
                       account_number_get: int, amount):

        self.users['accounts'][account_number_send].fund_transfer(
            amount=amount, account_number_o=account_number_get,
            types='withdraw')
        self.users['accounts'][account_number_get].fund_transfer(
            amount=amount, account_number_o=account_number_send,
            types='deposit')

    def account_history(self, account_number: int, types=None):
        '''
        transfer_history(account_number=integer,types=(withdraw,deposit,fund_transfer))
        return all history if not specified else return specified history
        '''
        if types is None:
            return (j for i in self.users['accounts'][
                account_number].history.values() for j in i.items())
        return (i for i in self.users['accounts'][
            account_number].history[types].items())

    def get_account_numbers(self, username: str):
        ''' return list of accounts number'''

        return (i for i in self.users['customers'][username].accounts)

    def all_accounts(self, username: str):
        '''return accounts obj'''
        accounts = self.get_account_numbers(username)
        return (self.users['accounts'][i] for i in accounts)

    def del_account(self, account_number: int):
        owner = self.users['accounts'][account_number].owner
        self.users['customers'][owner].accounts.remove(account_number)
        del self.users['accounts'][account_number]

    def search_account(self, account_number):
        if account_number in self.users['accounts']:
            return self.users['accounts'][account_number]
        return 2  # there is no such a account_number

# =========================customer part===============================

    def customer_history(self, username: str):
        return (j for i in self.users['customers'][
            username].history.values() for j in i.items())

    def create_customer(self, first_name: str, last_name: str, username: str,
                        password: str, ID: str, address: str):
        '''
        Customer(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string)
        return 4 if username exists else return object of customer
        '''
        if username not in self.users['customers']:
            customer = Customer(first_name=first_name, last_name=last_name,
                                username=username, password=password,
                                ID=ID, address=address)
            self.users['customers'][username] = customer
            return customer
        return 4  # the username is already exists

    def get_all_customers(self):
        return (i for i in self.user['customers'].values())

# ==========================manager part===============================
    def create_manager(self, first_name: str, last_name: str, username: str,
                       password: str, ID: str, address: str, salary: int):
        '''
        Manager(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string,salary:integer)
        return manager obj if already not exists
        else return 4(username already exists)
        '''
        if username not in self.users['managers']:
            manager = Manager(first_name=first_name, last_name=last_name,
                              username=username, password=password, ID=ID,
                              address=address, salary=salary)
            self.users['managers'][username] = manager
            return manager
        return 4  # username laready exists

    def get_all_managers(self):
        return (i for i in self.users['managers'].values())

# ==========================employee part==============================
    def get_all_employees(self):
        return (i for i in self.users['employees'].values)

    def create_employee(self, first_name: str,
                        last_name: str, username: str,
                        password: str, ID: str,
                        address: str, salary: int):
        '''
        Employee(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string,salary:integer)
        return 4 if username already exists else return employee obj
        '''
        if username not in self.users['employees']:
            employee = Employee(first_name=first_name, last_name=last_name,
                                username=username, ID=ID, password=password,
                                address=address, salary=salary)
            self.users['employees'][username] = employee
            return employee
        return 4  # username already exists

    def del_employee(self, username):
        if username in self.users['employee']:
            del self.users['employee'][username]
        else:
            return 3  # there is no such a username

# ==========================branch part===============================
    def create_branch(self, username: str, address: str):
        """
        branch(username=string,address=string)
        return 4 if username already exists else return object
        """
        if username not in self.users['branches']:
            branch = Branch(username=username, address=address)
            self.users['branches'][username] = branch
            return branch
        return 4  # username already exists

    def del_branch(self, username: str):
        if username in self.users['branches']:
            del self.users['branches'][username]
        else:
            return 3  # there is no such a username

    def add_branch_employee(self, branch_name, username):
        """
        add_branch_employee(branch_name=string,
        username=string must be in users[employees])
        """
        if branch_name not in self.users['branches']:
            return 6  # there is no such a branch
        if username not in self.users['employees']:
            return 3  # there is no such a username
        self.users['branches'][branch_name].employees.append(username)

    def change_branch(self, branch_name, **kwargs):
        if branch_name in self.users['branches']:
            for key, value in kwargs.items():
                if key in vars(self.users['branches'][branch_name]):
                    self.users['branches'][branch_name].key = value
        else:
            return 6  # there is no such a branch

    def get_branch_employees(self, branch_name):
        if branch_name in self.users['branches']:
            return (i for i in self.users['branches'][branch_name].employees)
        return 6  # there is no such a branch

    def set_branch_manager(self, branch_name, username):
        """set_branch_manager(branch_name=must be in users[branch],
        username=must be in users[managers])"""

        if branch_name not in self.users['branches']:
            return 6  # there is no such a branch
        if username not in self.users['managers']:
            return 3  # there is no such a username
        self.users['branches'][branch_name].manager = username
