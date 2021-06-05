# by Esmail
# here we define one class which presents a user that has logged in :)
from DS import Core  # just for type hint


# methods are callbacks
class User:
    def __init__(self, username: str, password: str,
                 types: str, database: Core):
        self.current_user = username
        self.current_password = password
        self.database = database
        self.types = types

    # ====================== Admin callback =========================
    def change_admin_info_callback(self, username=None, password=None,
                                   _type="admin"):
        if username:
            adm = self.database.change_username(self.current_user, username,
                                                _type)
            return adm
        elif password:
            adm = self.database.change_password(self.current_user,
                                                self.current_password,
                                                password, _type)
            return adm

    def new_branch_callback(self, name, address):
        brn = self.database.create_branch(name, address)
        if brn == 4:
            return 4

    def del_branch_callback(self, name):
        brn = self.database.del_branch(name)
        if brn == 3:
            return 3

    def change_branch_callback(self, old_name, name=None, address=None):
        brn = self.database.user_detail_change(old_name, "branches", name=name,
                                               address=address)
        self.database.change_username(old_name, name, "branches")
        if brn == 6:
            return 6

    def new_manager_callback(self, name, _id, username, password):
        mng = self.database.create_manager(name, name, username, password, _id,
                                           address="", salary=0)
        if mng == 4:
            return 4
        else:
            return mng

    def set_manager_callback(self, branch_name, manager_username):
        mng = self.database.set_branch_manager(branch_name, manager_username)
        if mng == 6:
            return 6
        if mng == 3:
            return 3

    def change_manager_callback(self, old_username, _id=None, username=None,
                                password=None, name=None):
        mng = self.database.user_detail_change(old_username,
                                               self.types,
                                               ID=_id,
                                               first_name=name,
                                               new_username=username,
                                               new_password=password)
        return mng

    def del_manager_callback(self):
        pass

    # ======================= Manager callback ===========================
    def change_employee_callback(self, old_username, username=None, _id=None,
                                 password=None, name=None):
        emp = self.database.user_detail_change(old_username,
                                               self.types,
                                               new_username=username,
                                               ID=_id, new_password=password,
                                               first_name=name)
        return emp

    def search_manager_callback(self, username):
        user = self.database.search_user(username)
        if user == 3:
            return 3
        else:
            return [user.name, user.id]

    def add_employee_callback(self, name, username, _id, password):
        employee = self.database.create_employee(name, name, username,
                                                 password, _id,
                                                 address="", salary=0)
        if employee == 4:
            return 4

    def del_employee_callback(self, username):
        employee = self.database.del_employee(username=username)
        if employee == 3:
            return 3

    def all_employee_callback(self):
        user = self.database.get_all_employees()
        for employee in user:
            yield [employee.first_name, employee.username]

    def set_my_info_callback(self):
        pass

    def open_panel_employee_callback(self, username):
        pass

    # ====================== Customer callback ==========================
    def receive_cash_callback(self, account_number, amount):
        account_number = self.database.search_account(account_number)
        if account_number == 2:
            return 2
        else:
            self.database.withdraw(account_number, amount)

    def all_accounts_callback(self):
        account_numbers = self.database.all_accounts(self.current_user)
        yield from ((number, self.database.get_balance(number))
                    for number in account_numbers)

    def transfer_callback(self, account_number, destination_number, amount):
        account_number = self.database.search_account(account_number)
        if account_number == 2:
            return 2
        else:
            self.database.funds_transfer(account_number,
                                         destination_number, amount)

    def get_history_callback(self, account_number):
        account_number = self.database.search_account(account_number)
        if account_number == 2:
            return 2
        else:
            return self.database.account_history(account_number)

    def change_info_callback(self, username=None, password=None):
        cus = self.database.user_detail_change(self.current_user,
                                               self.types,
                                               new_username=username,
                                               new_password=password)
        return cus

    # ===================== employee callback =========================
    def all_customers_callback(self):
        cus = self.database.get_all_customers()
        for customer in cus:
            yield [customer.first_name, customer.ID]

    def search_customers_callback(self, text):
        pass

    def get_account_callback(self, username):
        acc = self.database.get_account_numbers(username)
        return acc

    def del_account_callback(self, account_number):
        self.database.del_account(account_number)

    def deposit_callback(self, account_number, amount):
        self.database.deposit(account_number, amount)

    def get_customer_info_callback(self, username, _type="customer"):
        cus = self.database.search_user(username, _type)
        if cus == 3:
            return 3
        else:
            return [cus.first_name, cus.ID, cus.birthday]

    def set_customer_info_callback(self, old_username, username=None, _id=None,
                                   name=None, birthday=None,
                                   password=None):
        cus = self.database.user_detail_change(old_username,
                                               self.types,
                                               new_username=username,
                                               new_password=password,
                                               first_name=name,
                                               birthday=birthday, ID=_id)
        return cus

    def open_customer_panel_callback(self, username):
        pass

    def creat_customer_callback(self, name, username, _id, birthday, password):
        cus = self.database.create_customer(name, name, username, password,
                                            _id, birthday)
        if cus == 4:
            return 4

    def set_my_info_employee(self, username=None, password=None):
        if username:
            emp = self.database.change_username(self.current_user, username,
                                                "employee")
            return emp
        elif password:
            emp = self.database.change_password(self.current_user,
                                                self.current_password,
                                                password, "employee")
            return emp

    # ================================ Branch =================================

    def all_branch_callback(self):
        pass

    # ================================ Login =================================
    # login = LoginView(callback=check_login)
    # login.mainloop()
