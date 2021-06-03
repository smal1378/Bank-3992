# this file is going to connect DS module and GUI
from GUI import manager_view
from AdminView import AdminView
from DS import Core

dict_error = {
    1: 'There is not enough money in your account',
    2: 'There is no such a account number ',
    3: 'There is no such a username ',
    4: 'The username is already exist',
    5: 'Password is wrong',
    6: 'There is no such a branch',
    7: 'number is smaller or equal to 0'
}

database = Core()

current_user = None
current_password = None


def check_login(username, password, type):
    global current_user
    global current_password
    user = database.check_login(username, password, type)
    if user == 3:
        return 3
    elif type == "customer":
        current_user = username
        pass
    elif type == "employee":
        current_user = username
        pass
    elif type == "admin":
        current_user = username
        current_password = password
        admin_panel = AdminView(username, )
        admin_panel.mainloop()
    else:
        current_user = username
        mng = search_manager_callback(username)
        man_panel = manager_view.ManagerView(name=mng.first_name, username=current_user,
                                             list_employees=all_employee_callback,
                                             callback1=add_employee_callback,
                                             callback2=del_employee_callback,
                                             callback3=change_employee_callback, callback4=open_panel_employee_callback,
                                             callback5=search_manager_callback, callback6=set_my_info_callback)
        man_panel.mainloop()


# ================================ Admin callback =================================
def change_admin_info_callback(username=None, password=None, type="admin"):
    if username:
        adm = database.change_username(current_user, username, type)
        return adm
    elif password:
        adm = database.change_password(current_user, current_password, password, type)
        return adm


def new_branch_callback(name, address):
    brn = database.create_branch(name, address)
    if brn == 4:
        return 4


def del_branch_callback(name):
    brn = database.del_branch(name)
    if brn == 3:
        return 3


def change_branch_callback(old_name, name=None, address=None):
    brn = database.change_branch(old_name, new_name=name, address=address)
    if brn == 6:
        return 6


def new_manager_callback(name, id, username, password):
    mng = database.create_manager(name, name, username, password, id, address="", salary=0)
    if mng == 4:
        return 4
    else:
        return mng


def set_manager_callback(branch_name, manager_username):
    mng = database.set_branch_manager(branch_name, manager_username)
    if mng == 6:
        return 6
    if mng == 3:
        return 3


def change_manager_callback(old_username, id=None, username=None, password=None, name=None):
    mng = database.user_detail_change(old_username, ID=id, first_name=name, new_username=username,
                                      new_password=password)
    return mng


def del_manager_callback():
    pass


# ================================ Manager callback =================================
def change_employee_callback(old_username, username=None, id=None, password=None, name=None):
    emp = database.user_detail_change(old_username, new_username=username, ID=id, new_password=password,
                                      first_name=name)
    return emp


def search_manager_callback(username):
    user = database.search_user(username)
    if user == 3:
        return 3
    else:
        return [user.name, user.id]


def add_employee_callback(name, username, ID, password):
    employee = database.create_employee(name, name, username, password, ID, address="", salary=0)
    if employee == 4:
        return 4


def del_employee_callback(username):
    employee = database.del_employee(username=username)
    if employee == 3:
        return 3


def all_employee_callback():
    user = database.get_all_employees()
    for employee in user:
        yield [employee.first_name, employee.username]


def set_my_info_callback():
    pass


def open_panel_employee_callback(username):
    pass


# ================================ Customer callback =================================
def receive_cash_callback(account_number, amount):
    account_number = database.search_account(account_number)
    if account_number == 2:
        return dict_error[2]
    else:
        database.withdraw(account_number, amount)


def all_accounts_callback():
    account_number = database.all_accounts(current_user)
    return account_number


def transfer_callback(account_number, destination_number, amount):
    account_number = database.search_account(account_number)
    if account_number == 2:
        return dict_error[2]
    else:
        database.funds_transfer(account_number,
                                destination_number, amount)


def get_history_callback(account_number):
    account_number = database.search_account(account_number)
    if account_number == 2:
        return dict_error[2]
    else:
        return database.account_history(account_number)


def change_info_callback(username=None, password=None):
    cus = database.user_detail_change(current_user, new_username=username, new_password=password)
    return cus


# ================================ employee callback =================================
def all_customers_callback():
    cus = database.get_all_customers()
    for customer in cus:
        yield [customer.first_name, customer.ID]


def search_customers_callback(text):
    pass


def get_account_callback(username):
    acc = database.get_account_numbers(username)
    return acc


def del_account_callback(account_number):
    database.del_account(account_number)


def deposit_callback(account_number, amount):
    database.deposit(account_number, amount)


def get_customer_info_callback(username, type="customer"):
    cus = database.search_user(username, type)
    if cus == 3:
        return 3
    else:
        return [cus.first_name, cus.ID, cus.birthday]


def set_customer_info_callback(old_username, username=None, id=None, name=None, birthday=None,
                               password=None):
    cus = database.user_detail_change(old_username, new_username=username, new_password=password, first_name=name,
                                      birthday=birthday, ID=id)
    return cus


def open_customer_panel_callback(username):
    pass


def creat_customer_callback(name, username, id, birthday, password):
    cus = database.create_customer(name, name, username, password, id, birthday)
    if cus == 4:
        return 4


def set_my_info_employee(username=None, password=None):
    if username:
        emp = database.change_username(current_user, username, "employee")
        return emp
    elif password:
        emp = database.change_password(current_user, current_password, password, "employee")
        return emp


# ================================ Branch =================================


def all_branch_callback():
    pass

# ================================ Login =================================
# login = LoginView(callback=check_login)
# login.mainloop()
