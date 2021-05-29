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
              4: 'The username  already exists',
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
        return True if admin else False
        return object if exists
        else return 3 (There is no such a username)

        '''
        users = self.users[types]
        if types == 'admin':
            return users['username'] == username and (
                users['password'] == password)
        if username in users and (
                password == users[username].password):
            return users[username]
        return 3  # There is no such a username

    def change_username(self, old_username, new_username, types):
        '''
        change_username(old_username=string,new_username=string,types=(customers,branches,employees,managers))
        return 4 if username already exists
        return 3 if There is no such a username
        '''
        users = self.users[types]
        if new_username in users:
            return 4  # username already exists
        if users.get(old_username):
            users[new_username] = users.pop(old_username)
            setattr(users[new_username], 'username', new_username)
            if types == 'customers':
                for account in users[new_username].accounts:
                    setattr(self.users['accounts'][account],
                            'owner', new_username)
        else:
            return 3  # There is no such a username

    def change_password(self, username: str, old_password: str,
                        new_password: str, types):
        '''
        change_password(username=string,old_paasword=string,new_password=str,
        types=(customers,branches,employees,managers))
        return 5 if password is wrong
        '''
        user = self.users[types][username]
        if old_password == user.password:
            setattr(user, 'password', new_password)
        else:
            return 5  # password is wrong

    def search_user(self, username: str, types=None, only_with_types=False):
        '''
        search_user(username=string,types=(customers,branches,employees,managers))
        return an object if exist else return 3 '''
        result = []
        if self.users.get(types):
            user_ = self.users.get(types).get(username)
            return user_ if user_ else 3
        if not only_with_types:
            for group in self.users:
                user = self.users[group].get(username)
                if user:
                    result.append(user)
        return result if result else 3  # thereis no such a username

    def user_detail_change(self, username, types, **kwargs):
        '''
        User(first_name=string,last_name=string,ID=string,address=string)
        Manager(salary=integer)
        employee(salary=integer)
        '''
        user = self.search_user(username, types, only_with_types=True)
        if user == 3:
            return 3  # there is no such a username
        for key, value in kwargs.items():

            if hasattr(user, key):
                setattr(user, key, value)

# ==========================account part================================

    def create_account(self, username: str, amount=0):
        '''
        create_account(self,username=string and must be in users[customers],
        amount=default 0)
        get username and return integer(account_number)
        '''
        accounts = self.users['accounts']
        customers = self.users['customers']
        if username not in customers:
            return 3  # There is no such a username

        while True:
            account_number = randint(10**16, (10**17)-1)

            if account_number not in accounts:
                # add to accounts attribute in customer class
                customers[username].add_account(account_number)
                # save account object in users[accounts]
                accounts[account_number] = Account(
                    balance=amount, account_number=account_number,
                    owner=username)
                return account_number

    def deposit(self, account_number: int, amount: int):

        return self.users['accounts'][account_number].deposit(amount)

    def get_balance(self, account_number):
        account = self.users['accounts'].get(account_number)
        if account:
            return account.show_balance()
        return 2  # there is no such a account_number

    def withdraw(self, account_number: int, amount: int):
        return self.users['accounts'][account_number].withdraw(amount)

    def funds_transfer(self, sender: int, receiver: int, amount: int):
        """
        funds_transfer(sender=account number of sender,
        receiver=account number of receiver,amount=integer)
        """
        send = self.users['accounts'][sender].fund_transfer(
            amount=amount, account_num=receiver, types='transfer_withdraw')
        if send:
            return send
        receive = self.users['accounts'][receiver].fund_transfer(
            amount=amount, account_num=sender,
            types='transfer_deposit')
        if receive:
            return receive

    def account_history(self, account_number: int, types=None):
        '''
        transfer_history(account_number=integer,types=(withdraw,deposit,fund_transfer))
        return all history if not specified else return specified history
        '''
        account = self.users['accounts'][account_number]
        if types is None:
            return (j for i in account.history.values() for j in i.items())
        return (i for i in account.history[types].items())

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
        account = self.users['accounts'].get(account_number)
        return account if account else 2  # There is no such a account_number

# =========================customer part===============================

    def customer_history(self, username: str):
        """ return histoy if username exists
        else 3 (there is no such a user name ) """
        customer = self.users['customers'].get(username)
        # there is no such a username
        return (j for i in customer.history.values() for j in i.items())\
            if customer else 3

    def create_customer(self, first_name: str, last_name: str, username: str,
                        password: str, ID: str, address: str):
        '''
        Customer(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string)
        return 4 if username exists else return object of customer
        '''
        var = vars()
        var.pop('self')
        if username not in self.users['customers']:
            customer = Customer(**var)
            self.users['customers'][username] = customer
            return customer
        return 4  # the username is already exists

    def get_all_customers(self):
        return (i for i in self.users['customers'].values())

# ==========================manager part===============================
    def create_manager(self, first_name: str, last_name: str, username: str,
                       password: str, ID: str, address: str, salary: int):
        '''
        Manager(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string,salary:integer)
        return manager obj if already not exists
        else return 4(username already exists)
        '''
        var = vars()
        var.pop('self')
        if username not in self.users['managers']:
            manager = Manager(**var)
            self.users['managers'][username] = manager
            return manager
        return 4  # username laready exists

    def get_all_managers(self):
        return (i for i in self.users['managers'].values())

# ==========================employee part==============================
    def get_all_employees(self):
        return (i for i in self.users['employees'].values())

    def create_employee(self, first_name: str,
                        last_name: str, username: str,
                        password: str, ID: str,
                        address: str, salary: int):
        '''
        Employee(first_name:string ,last_name:string,username:string,
        password:string,ID:string,address:string,salary:integer)
        return 4 if username already exists else return employee obj
        '''
        var = vars()
        var.pop('self')
        if username not in self.users['employees']:
            employee = Employee(**var)

            self.users['employees'][username] = employee
            return employee
        return 4  # username already exists

    def del_employee(self, username):
        if username in self.users['employees']:
            del self.users['employees'][username]
        else:
            return 3  # there is no such a username

# ==========================branch part===============================
    def create_branch(self, name: str, address: str):
        """
        branch(name=string,address=string)
        return 4 if username already exists else return object
        """
        var = vars()
        var.pop('self')
        if name not in self.users['branches']:
            branch = Branch(**var)
            self.users['branches'][name] = branch
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

    def change_branch_details(self, branch_name, **kwargs):
        branches = self.users['branches']
        if branch_name in branches:
            for key, value in kwargs.items():
                if key == 'name':
                    branches[value] = branches.pop(branch_name)
                    branch_name = value
                if hasattr(branches[branch_name], key):
                    setattr(branches[branch_name], key, value)
        else:
            return 6  # there is no such a branch

    def get_branch_employees(self, branch_name):
        branches = self.users['branches']
        if branch_name in branches:
            return (i for i in self.users['branches'][branch_name].employees)
        return 6  # there is no such a branch

    def set_branch_manager(self, branch_name, username):
        """set_branch_manager(branch_name=must be in users[branch],
        username=must be in users[managers])"""
        branches = self.users['branches']
        if branch_name not in branches:
            return 6  # there is no such a branch
        if username not in self.users['managers']:
            return 3  # there is no such a username
        setattr(branches[branch_name], 'manager', username)
