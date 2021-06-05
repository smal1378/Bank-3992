from ..gui_configuration import Tk, Button, Frame
from GUI_Modules.manager.edit_user_view import EditUserView
from GUI_Modules.manager.edit_me_view import EditMeView
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from .Accounts_view import Accounts_view
from ..manager.add_user_view import AddUserView


class EmployeeView(Tk):
    """
    This class creates manager panel.
    Access to:
        edit_view panel
        edit_me panel
        add_user panel
    """

    def __init__(self, name, username, list_employees,
                 callback1=None, callback2=None,
                 callback3=None, callback4=None,
                 callback5=None, callback6=None,
                 callback7=None, callback8=None,
                 callback9=None, callback10=None):
        super(EmployeeView, self).__init__()
        self.name = name
        self.username = username
        self.list_employees = list_employees
        self.callback1 = callback1  # add_employee()
        self.callback2 = callback2  # remove_employee()
        self.callback3 = callback3  # change_employee
        self.callback4 = callback4  # open_employee_panel()
        self.callback5 = callback5  # search()
        self.callback6 = callback6  # add_account()
        self.callback7 = callback7  # get_accounts()
        self.callback8 = callback8  # remove_account()
        self.callback9 = callback9  # add_money()
        self.callback10 = callback10  # open_customer_panel()
        self.title(f"Panel manager: {self.name}")
        self.bind("<Configure>", self.auto_geometry)
        # self.icon (may add it)
        self.resizable(False, False)
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row=0, column=0)

        self.tab_main = Frame(self)
        self.tab_main.grid(row=0, column=0)
        self.tab_edit_me = Frame(self)
        self.tab_edit_me.grid(row=0, column=0)
        self.tab_add_user = Frame(self)
        self.tab_add_user.grid(row=0, column=0)
        self.tab_edit_user = Frame(self)
        self.tab_edit_user.grid(row=0, column=0)
        self.tab_accounts = Frame(self)
        self.tab_accounts.grid(row=0, column=0)
        self.tabs.add(self.tab_main, text="Main menu")

        # Defining Tab-main frames
        self.fr_aboutme = tk.LabelFrame(self.tab_main, text="About me",
                                        bg="gray")
        self.fr_aboutme.grid(row=0, column=0, rowspan=2, padx=10)
        self.fr_seachbar = Frame(self.tab_main)
        self.fr_seachbar.grid(row=0, column=1)
        self.fr_treev = Frame(self.tab_main)
        self.fr_treev.grid(row=1, column=1)
        self.fr_edit = Frame(self.tab_main)
        self.fr_edit.grid(row=1, column=2)

        # Frame about
        self.lbl_name = tk.Label(self.fr_aboutme, text="Name:")
        self.lbl_name.grid(row=0, column=0,
                           sticky="w", padx=10, pady=5)
        self.lbl_name = tk.Label(self.fr_aboutme, text=self.name)
        self.lbl_name.grid(row=0, column=1,
                           sticky="w", padx=10, pady=5)
        self.lbl_username = tk.Label(self.fr_aboutme, text="Username:")
        self.lbl_username.grid(row=1, column=0,
                               sticky="w", padx=10, pady=5)
        self.lbl_username = tk.Label(self.fr_aboutme, text=self.username)
        self.lbl_username.grid(row=1, column=1,
                               sticky="w", padx=10, pady=5)
        self.btn_edit_me = Button(self.fr_aboutme, text="Edit",
                                  command=self.edit_me,
                                  relief=tk.GROOVE)
        self.btn_edit_me.grid(row=2, column=0, columnspan=2, pady=5)

        # Frame search bar
        self.search_bar = tk.Entry(self.fr_seachbar, width=50)
        self.search_bar.grid(row=0, column=0, pady=10)
        self.btn_search = Button(self.fr_seachbar, text="search",
                                 command=self.search_treev)
        self.btn_search.grid(row=0, column=1, padx=5)
        self.btn_refresh = Button(self.fr_seachbar, text="Refresh",
                                  command=self.refresh_treev)
        self.btn_refresh.grid(row=0, column=2)

        # Frame list
        self.users_treev = ttk.Treeview(self.fr_treev, selectmode='browse',
                                        height=15)
        self.users_treev.grid(row=0, column=0)
        self.users_treev['columns'] = ("1", "2")
        self.numeric_columns = ("2",)  # used to sort columns properly
        self.users_treev["show"] = "headings"
        self.users_treev.column("1", width=140, anchor='c')
        self.users_treev.column("2", width=140, anchor='c')

        self.users_treev.heading("1", text="Name",
                                 command=lambda:
                                 self.treev_cl_sort("1", False))
        self.users_treev.heading("2", text="ID",
                                 command=lambda:
                                 self.treev_cl_sort("2", False))

        self.scrollbar = ttk.Scrollbar(self.fr_treev,
                                       command=self.users_treev.yview,
                                       orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1)
        self.users_treev.configure(xscrollcommand=self.scrollbar.set)

        # Frame edit
        self.btn_add_user = Button(self.fr_edit, text="Add user",
                                   command=self.add_user)
        self.btn_add_user.grid(row=0, column=0)
        self.btn_edit_user = Button(self.fr_edit, text="Edit user",
                                    command=self.edit_user)
        self.btn_edit_user.grid(row=1, column=0, pady=10, padx=10)
        self.btn_delete_user = Button(self.fr_edit, text="Delete user",
                                      command=self.del_user)
        self.btn_delete_user.grid(row=2, column=0)
        self.btn_accounts = Button(self.fr_edit, text="Accounts",
                                   command=self.open_accounts)
        self.btn_accounts.grid(row=3, column=0, pady=10)

        for user in self.list_employees:
            self.users_treev.insert("", "end", values=user)
        self.users_treev.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        """
        assigning a double-click function to treev to open their panel.
        """

        user = self.users_treev.selection()
        if user == ():  # double click on headings or any other empty space
            return None
        name, id_ = self.users_treev.item(user)["values"]  # = (name, id)
        if self.callback10:
            self.callback10(id_)
        self.users_treev.selection_remove(user[0])  # clear selection

    def edit_me(self):
        children = self.tab_edit_me.winfo_children()
        if children != []:  # if a edit_view panel is open then ignore.
            return None
        panel = EditMeView(self.username, self.tab_edit_me, self.callback6,
                           self.close_tab, self.msg_err)

        self.tabs.add(self.tab_edit_me, text="Edit-me menu")

    def add_user(self):
        children = self.tab_add_user.winfo_children()
        if children:  # if a edit_view panel is open then ignore.
            return None
        panel = AddUserView(self.tab_add_user, self.callback1,
                            self.close_tab, self.msg_err)
        self.tabs.add(self.tab_add_user, text="Add-user")

    def del_user(self):
        selected = self.users_treev.focus()  # returns selected item ID
        if selected == "":  # nothig selected, but btn is ckicked
            return None
        name, username = self.users_treev.item(selected, "values")
        self.users_treev.delete(selected)
        if self.callback2:
            self.callback2(username, self.msg_err)
        # update self.list_emplyees

    def edit_user(self):
        children = self.tab_edit_user.winfo_children()
        if children:
            for widget in children:  # widget = last EditUserView()
                widget.destroy()
        selected = self.users_treev.focus()
        if selected == "":  # nothing selected, but btn is clicked
            return None
        name, username = self.users_treev.item(selected, "values")
        panel = EditUserView(name, username, self.tab_edit_user,
                             self.callback3, self.close_tab, self.msg_err)
        self.tabs.add(self.tab_edit_user, text=f"Edit {name}")
        # update self.list_employees (update by order of main.py).
        # update treeview. call refresh_treev after list update.
        self.users_treev.selection_remove(selected)

    def open_accounts(self):
        user = self.users_treev.selection()
        if user == ():  # double click on headings or any other empty space
            return None
        name, id_ = self.users_treev.item(user)["values"]  # = (name, id)
        panel = Accounts_view(id_, self.tab_accounts, self.callback6,
                              self.callback7,
                              self.callback8,
                              self.callback9)
        self.tabs.add(self.tab_accounts, text="Accounts-view")
        self.users_treev.selection_remove(user[0])  # clear selection

    def refresh_treev(self):
        self.users_treev.delete(*self.users_treev.get_children())
        for user in self.list_employees:
            self.users_treev.insert("", "end", values=user)

    def search_treev(self):  # key could be anything
        text = self.search_bar.get()
        if self.callback5:
            matched_items = self.callback5(text)
            if len(matched_items) > 0:
                self.users_treev.delete(*self.users_treev.get_children())
                for item in matched_items:
                    self.users_treev.insert("", "end", values=item)
            else:
                self.msg_err("Error", "User not found")

    def treev_cl_sort(self, col, reverse):
        """ click on each heading to sort by the values of it."""

        users = [(self.users_treev.set(id_, col), id_)
                 for id_ in self.users_treev.get_children()]
        # users = [(value 1, id-row 1), (value 2, id-row 2), ...]
        users.sort(reverse=reverse)  # sorted by values. not row-id !
        for index, (val, id_) in enumerate(users):
            self.users_treev.move(id_, '', index)
        self.users_treev.heading(col, command=lambda:
                                 self.treev_cl_sort(col, not reverse))

    def close_tab(self):
        """
        just closing the tab.
        used as callback for all tabs like edit_view, edit_me, etc.
        """

        self.tabs.forget(self.tabs.select())

    def run(self):
        self.mainloop()

    def close(self):
        self.destroy()

    def msg_err(self, title=None, msg=None, master=None):
        if master is None:
            master = self
        tk.messagebox.showerror(title, msg, parent=master)


if __name__ == "__main__":
    import random

    lst = [(f"user {i + 1}", random.randint(10 ** 11, (10 ** 12) - 1)) \
           for i in range(20)]
    panel = EmployeeView("siamak", "siamak_sdi", lst)
    panel.run()
