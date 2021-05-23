
# Core:
###### global users:
- user_detail_change(username, **kwargs)
- get_user(username)
###### branchs:
- create_branch(name, address)
- del_branch(name)
- change_branch(name, new_name=None, new_address=None)
- all_branch_employees(branch_name)
- set_branch_manager(branch_name, manager_username)
###### accounts:
- create_account(username, amount=0) -> account_number
- del_account(account_number)
- deposit(account_number, amount)
- withdraw(account_number, amount)
- get_balance(account_number)
- funds_transfer(account_number_sender, account_number_receiver, amount)
- transfer_history(account_number)
- get_account_numbers(username)
###### customers:
- create_customer(name, username, id, birthday, password)
- search_customers(text)
- all_customers()
###### managers:
- create_manager(name, id, username, password)
- all_managers()
###### employees:
- create_employee(name, id, username, password)
- del_employee(username)
- all_employees()
###### other:
- check_login(username, password) -> user_object


# GUI Admin Callbacks:
- change_admin_info(username=None, password=None)
- new_branch(name, address)
- del_branch(name)
- change_branch(old_name, name=None, address=None)
- all_employees() -> list[(name, username)]
- all_customers() -> list[(name, username)]
- all_managers() -> list[(name, username)]
- new_manager(name, id, username, password)
- set_manager(branch_name, manager_username)
- change_manager(old_username, id=None, username=None, password=None, name=None)
- del_manager(username)  # omit for now 

# GUI Manager Callbacks:
- add_employee(name, username, id, password)
- del_employee(username)
- all_employees() -> list[(name, username)]
- change_employee(old_username, username=None, id=None, password=None, name=None)
- open_employee_panel(username)

# GUI Customer Callbacks:
- all_accounts() # this will only return account numbers for this customer
- receive_cash(account_number, amount)
- transfer(account_number, destination_number, amount)
- get_history(account_number) -> list[string]
- change_info(username=None, password=None)

# GUI Employee Callbacks:
- all_customers() -> list[(name, id)]
- search_customers(text) -> list[(name, id)]
- add_account(username) -> account_number
- get_accounts(username) -> list[(account_number, remaining)]
- del_account(account_number)
- deposit(account_number, amount)
- get_customer_info(username) -> (name, id, birthday)
- set_customer_info(old_username, username=None, id=None, name=None, birthday=None, password=None)
- open_customer_panel(username)
- create_customer(name, username, id, birthday, password)
- set_my_info(username=None, password=None)
