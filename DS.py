"""
in This Module we define an api for the main.py
methods in Core object must be able to do anything we need the backend do
other classes, functions or constants can be defined for internal use.
"""
from DSModels import Account, Customer, Branch, Employee, Manager, Admin
from dataclasses import dataclass
from random import randint

dict_error = {
    1: "There is not enough money in your account",
    2: "There is no such a account number ",
    3: "There is no such a username ",
    4: "The username  already exists",
    5: "Password is wrong",
    6: "There is no such a branch",
    7: "number is smaller or equal to 0",
}


@dataclass
class Core:
    """
    Core part of DS
    """

    __default_admin = Admin("admin", "admin")
    __users = {
        "customers": {},
        "employees": {},
        "accounts": {},
        "branches": {},
        "admin": {"admin": __default_admin},
        "managers": {},
    }
    # ============================admin part=================================

    def set_admin(self, username: str, password: str):
        """set_admin also can be used for change password or username"""
        self.__users["admin"][username] = Admin(username, password)

    # ===========================global part=================================

    def check_login(self, username: str, password: str, types: str):
        """
        check_login(username=string,password=string,
        type=(customers,empolyees,managers,admin))
        return object if exists
        else return 3 (There is no such a username)
        """
        user = self.__users[types].get(username)
        if user and (password == user.password):
            return user
        return 3  # There is no such a username

    def change_username(self, old_username: str, new_username: str, types):
        """
        change_username(old_username=string,new_username=string,
        types=(customers,branches,employees,managers,admin))
        return 4 if username already exists
        return 3 if There is no such a username
        """
        users = self.__users[types]
        if new_username in users:
            return 4  # username already exists
        if old_username in users:
            users[new_username] = users.pop(old_username)
            user = users[new_username]
            setattr(user, "username", new_username)

            if types == "customers":
                for account in user.accounts:
                    setattr(self.__users["accounts"]
                            [account], "owner", new_username)

            if types == "branches":
                for employee in user.employees:
                    employee = self.__users["employees"][employee]
                    setattr(employee, "branch", new_username)
        else:
            return 3  # There is no such a username

    def change_password(
        self, username: str, old_password: str, new_password: str, types
    ):
        """
        change_password(username=string,old_paasword=string,new_password=str,
        types=(customers,employees,managers,admin))
        return 5 if password is wrong
        """
        user = self.__users[types][username]
        if old_password == user.password:
            setattr(user, "password", new_password)
        else:
            return 5  # password is wrong

    def search_user(self, username: str, types=None, only_with_types=False):
        """
        search_user(username=string,types=(customers,branches,employees,managers)
        only_with_types=True if only search with type)
        return an object if exist else return 3"""
        result = []
        if self.__users.get(types):
            user_ = self.__users.get(types).get(username, 3)
            return user_
        if not only_with_types:
            for group in self.__users:
                user = self.__users[group].get(username)
                if user:
                    result.append(user)
        return result if result else 3  # thereis no such a username

    def user_detail_change(self, username, types, **kwargs):
        """
        User(first_name=string,last_name=string,
        ID=string,address=string,password=string)
        Manager(salary=integer)
        employee(salary=integer)
        admin(password=string)
        branch(address)
        """
        user = self.search_user(username, types, only_with_types=True)
        if user == 3:
            return 3  # there is no such a username
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)

    # ==========================account part================================

    def create_account(self, username: str, amount=0):
        """
        create_account(self,username=string and must be in users[customers],
        amount=default 0)
        get username and return integer(account_number)
        """
        accounts = self.__users["accounts"]
        customers = self.__users["customers"]
        if username not in customers:
            return 3  # There is no such a username

        while True:
            account_num = randint(10 ** 16, (10 ** 17) - 1)

            if account_num not in accounts:
                # add to accounts attribute in customer class
                customers[username].add_account(account_num)
                # save account object in users[accounts]
                accounts[account_num] = Account(
                    balance=amount, account_number=account_num, owner=username
                )
                return account_num

    def deposit(self, account_num: int, amount: int):

        return self.__users["accounts"][account_num].deposit(amount)

    def get_balance(self, account_num: int):
        """return balance if account exists
        else return 2 There is no such a account"""
        account = self.__users["accounts"].get(account_num)
        return account.show_balance() if account else 2

    def withdraw(self, account_num: int, amount: int):
        return self.__users["accounts"][account_num].withdraw(amount)

    def funds_transfer(self, sender: int, receiver: int, amount: int):
        """
        funds_transfer(sender=account number of sender,
        receiver=account number of receiver,amount=integer)
        return 1 if amount bigger than balance
        return 7 if amount is bigger or equal to 0
        """
        accounts = self.__users["accounts"]
        send = accounts[sender].fund_transfer(
            amount=amount, account_num=receiver, types="transfer_withdraw"
        )
        if send:
            return send
        receive = accounts[receiver].fund_transfer(
            amount=amount, account_num=sender, types="transfer_deposit"
        )
        if receive:
            return receive

    def account_history(self, account_num: int, types=None):
        """
        transfer_history(account_number=integer,types=(withdraw,deposit,fund_transfer))
        return all history if not specified else return specified history
        """
        account = self.__users["accounts"][account_num]
        return account.get_history(types=types)

    def get_account_numbers(self, username: str):
        """ return accounts number"""
        accounts = self.__users["customers"][username].accounts
        return map(lambda i: i, accounts)

    def all_accounts(self, username: str):
        """return accounts obj"""
        accounts_num = self.get_account_numbers(username)
        accounts = self.__users["accounts"]
        return map(lambda i: accounts[i], accounts_num)

    def del_account(self, account_num: int):
        account = self.__users["accounts"][account_num]
        customers = self.__users["customers"]
        customers[account.owner].accounts.remove(account_num)
        del account

    def search_account(self, account_num: int):
        """return object if account exists
        else 2 (there is no such a account number)"""
        account = self.__users["accounts"].get(account_num, 2)
        return account

    # =========================customer part===============================

    def customer_history(self, username: str, types=None):
        """return histoy if username exists
        else 3 (there is no such a user name )"""
        customer = self.__users["customers"].get(username)
        if customer:
            return customer.get_history(types=types)
        return 3  # there is no such a username

    def create_customer(
        self,
        first_name: str,
        last_name: str,
        username: str,
        password: str,
        ID: str,
        address: str,
    ):
        """
        return 4 if username exists
        else return object
        """
        var = vars()
        var.pop("self")
        customers = self.__users["customers"]
        if username not in customers:
            customer = Customer(**var)
            customers[username] = customer
            return customer
        return 4  # the username is already exists

    def get_all_customers(self):
        customers = self.__users["customers"].values()
        return map(lambda i: i, customers)

    # ==========================manager part===============================
    def create_manager(
        self,
        first_name: str,
        last_name: str,
        username: str,
        password: str,
        ID: str,
        address: str,
        salary: int,
    ):
        """
        return object if already not exists
        else return 4(username already exists)
        """
        var = vars()
        var.pop("self")
        managers = self.__users["managers"]
        if username not in managers:
            manager = Manager(**var)
            managers[username] = manager
            return manager
        return 4  # username laready exists

    def get_all_managers(self):
        managers = self.__users["managers"].values()
        return map(lambda i: i, managers)

    # ==========================employee part==============================
    def get_all_employees(self):
        employees = self.__users["employees"].values()
        return map(lambda i: i, employees)

    def create_employee(
        self,
        first_name: str,
        last_name: str,
        username: str,
        password: str,
        ID: str,
        address: str,
        salary: int,
    ):
        """
        return 4 if username already exists
        else return employee obj
        """
        var = vars()
        var.pop("self")
        employees = self.__users["employees"]
        if username not in employees:
            employee = Employee(**var)
            employees[username] = employee
            return employee
        return 4  # username already exists

    def del_employee(self, username: str):
        """return 3 if There is no such a username"""
        employee = self.__users["employees"].get(username)
        if employee:
            branch = employee.branch
            if branch:
                self.del_branch_employee(branch, username)
            del employee
        else:
            return 3  # there is no such a username

    # ==========================branch part===============================
    def create_branch(self, name: str, address: str):
        """
        return 4 if username already exists
        else return object
        """
        var = vars()
        var.pop("self")
        branches = self.__users["branches"]
        if name not in branches:
            branch = Branch(**var)
            branches[name] = branch
            return branch
        return 4  # username already exists

    def del_branch(self, username: str):
        branch = self.__users["branches"].get(username)
        if branch:
            for i in branch.employees:
                self.user_detail_change(i, "employees", branch="")
            del self.__users["branches"][username]
        else:
            return 3  # there is no such a username

    def add_branch_employee(self, branch_name: str, username: str):
        """
        add_branch_employee(branch_name=string,
        username=must be in users[employees])
        """
        branch = self.__users["branches"].get(branch_name)
        employee = self.__users["employees"].get(username)
        if not branch:
            return 6  # there is no such a branch
        if not employee:
            return 3  # there is no such a username
        branch.employees.append(username)
        setattr(employee, "branch", branch_name)

    def del_branch_employee(self, branch_name: str, username: str):
        """
        return 6 if there is no such a branch
        return 3 if there is no such a username
        """
        branch = self.__users["branches"].get(branch_name)
        employee = self.__users["employees"].get(username)
        if not branch:
            return 6  # there is no such a branch
        if not employee:
            return 3  # there is no such a username
        employees = branch.employees
        if username in employees:
            employees.remove(username)

    def get_branch_employees(self, branch_name):
        """
        return 6 if there is no such a branch
        else return branch employees"""
        branch = self.__users["branches"].get(branch_name)
        if branch:
            employees = branch.employees
            return map(lambda i: i, employees)
        return 6  # there is no such a branch

    def set_branch_manager(self, branch_name, username):
        """set_branch_manager(branch_name=must be in users[branch],
        username=must be in users[managers])
        return 6 if there is no such a branch
        return 3 if there is no such a username"""
        branches = self.__users["branches"]
        manager = self.__users["managers"].get(username)
        if branch_name not in branches:
            return 6  # there is no such a branch
        if not manager:
            return 3  # there is no such a username
        setattr(branches[branch_name], "manager", username)

    def get_all_branches(self):
        branches = self.__users["branches"].values()
        return map(lambda i: i, branches)
