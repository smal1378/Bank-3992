# this file is going to connect DS module and GUI_Modules
from GUI import AdminView, CustomerView, EmployeeView, ManagerView, LoginView
from DS import Core, dict_error
from pickle import load, dump
from os.path import exists as file_exists
from main_user import User

if file_exists("database.bin"):
    file = open("database.bin", "rb")
    database = load(file)
    file.close()
else:
    database = Core()


def check_login(username, password):
    output = database.check_login(username, password)
    if output == 3:
        login.show_error(dict_error[3])
        return
    else:
        user, _type = output
        _user = User(username, password, _type, database)
    if _type == "customer":
        mng = database.search_user(username)
        panel = CustomerView(name=mng.first_name,
                             username=username,
                             balance=0,  # this should be removed
                             list_transaction=[],  # should be removed
                             callback1=_user.all_accounts_callback,
                             callback2=_user.receive_cash_callback,
                             callback3=_user.transfer_callback,
                             callback4=_user.get_history_callback,
                             callback5=_user.change_info_callback,
                             )
        panel.mainloop()
    elif _type == "employee":
        pass
    elif type == "admin":
        pass
    elif type == "manager":
        mng = database.search_user(username)
        man_panel = ManagerView(name=mng.first_name,
                                username=username,
                                list_employees=_user.all_employee_callback(),
                                callback1=_user.add_employee_callback,
                                callback2=_user.del_employee_callback,
                                callback3=_user.change_employee_callback,
                                callback4=_user.open_panel_employee_callback,
                                callback5=_user.search_manager_callback,
                                callback6=_user.set_my_info_callback)
        man_panel.mainloop()
    else:
        # means wrong password
        login.show_error("This code should never get reached!")


login = LoginView(check_login)
login.mainloop()

file = open("database.bin", "wb")
dump(database, file)
file.close()
