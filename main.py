# this file is going to connect DS module and GUI
from manager_view import ManagerView
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


def check_login(username, password, type):
    user = database.check_login(username, password, type)
    if user == 3:
        return 3
        # login.show_error("incorrect password or username!")
    elif type == "customer":
        pass
    elif type == "employee":
        pass
    elif type == "admin":
        pass
    else:
        man_panel = ManagerView(callback1=add_employee_callback, callback2=del_employee_callback,
                                callback3=change_employee_callback, callback4=open_panel_employee_callback,
                                callback5=search_manager_callback)
        man_panel.mainloop()


# ================================ Admin callback =================================
# ================================ Manager callback =================================
def change_employee_callback(old_username, type=None, username=None, id=None, password=None, name=None):
    pass


def search_manager_callback(username):
    user = database.search_user(username)
    if user == 3:
        return 3
    else:
        return [(user.name, user.id)]



def add_employee_callback(name, username, ID, password):
    employee = database.create_employee(name, username, ID, password)
    if employee == 4:
        return 4


def del_employee_callback(username):
    employee = database.del_employee(username=username)
    if employee == 3:
        return 3


def all_employee_callback():
    user = database.get_all_employees()
    for employee in user:
        yield [(employee.first_name, employee.username)]


def open_panel_employee_callback(username):
    pass

# ================================ Customer callback =================================
# ================================ employee callback =================================
# ================================ Login =================================
# login = LoginView(callback=check_login)
# login.mainloop()
