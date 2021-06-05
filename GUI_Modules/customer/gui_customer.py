import tkinter as tk
from tkinter import ttk
from .Daryaft import Daryaft1
from .Enteghal import Enteghal1
from .Mojoodi import Mojoodi1
from .Edit import Edit1
from ..gui_configuration import Tk, Button, Frame, Label
import random
import time
import datetime
from random import randrange
from datetime import timedelta


class CustomerView(Tk):

    def __init__(self, name, username, balance, list_transaction,
                 callback1=None, callback2=None, callback3=None,
                 callback4=None, callback5=None):
        super().__init__()
        self.name = name
        self.username = username
        self.balance = balance
        self.list_transaction = list_transaction
        self.callback1 = callback1  # receive_cash()
        self.callback2 = callback2  # transfer()
        self.callback3 = callback3  # balance()
        self.callback4 = callback4  # get_history()
        self.callback5 = callback5  # # set_my_info()
        self.title(f"مدیریت صفحه مشتری: {self.name}")

        self.resizable(True, True)
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row=0, column=0)

        self.tab_main = Frame(self)
        self.tab_main.grid(row=0, column=0)
        self.tab_edit = Frame(self)
        self.tab_edit.grid(row=0, column=0)
        self.tab_Daryaft = Frame(self)
        self.tab_Daryaft.grid(row=0, column=0)
        self.tab_Enteghal = Frame(self)
        self.tab_Enteghal.grid(row=0, column=0)
        self.tab_Mojoodi = Frame(self)
        self.tab_Mojoodi.grid(row=0, column=0)
        self.tabs.add(self.tab_main, text="صفحه اصلی")

        self.fr_aboutme = tk.LabelFrame(self.tab_main, text="اطلاعات مشتری",
                                        bg="#828782")
        self.fr_aboutme.grid(row=1, column=2, rowspan=2, padx=10)
        self.fr_treev = Frame(self.tab_main)
        self.fr_treev.grid(row=1, column=1)
        self.fr_edit = Frame(self.tab_main)
        self.fr_edit.grid(row=1, column=0)

        self.lbl_name = Label(self.fr_aboutme, text="نام صاحب حساب:",
                              bg="#e4e8d5")
        self.lbl_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.lbl_name = Label(self.fr_aboutme, text=self.name, bg="#e4e8d5")
        self.lbl_name.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        self.lbl_username = Label(self.fr_aboutme,
                                  text="نام کاربری صاحب حساب:", bg="#e4e8d5")
        self.lbl_username.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.lbl_username1 = Label(self.fr_aboutme, text=self.username,
                                   bg="#e4e8d5")
        self.lbl_username1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.lbl_balance = Label(self.fr_aboutme, text="موجودی حساب:",
                                 bg="#e4e8d5")
        self.lbl_balance.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.lbl_balance1 = Label(self.fr_aboutme,
                                  text=f" {self.balance}ریال ", bg="#e4e8d5")
        self.lbl_balance1.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.users_treev = ttk.Treeview(self.fr_treev, selectmode='browse',
                                        height=15)
        self.users_treev.grid(row=0, column=0)
        self.users_treev['columns'] = ("1", "2", "3")
        self.users_treev["show"] = "headings"
        self.users_treev.column("1", width=140, anchor='c')
        self.users_treev.column("2", width=140, anchor='c')
        self.users_treev.column("3", width=140, anchor='c')

        self.users_treev.heading("1", text="تاریخ", command=lambda:
                                 self.treev_cl_sort("1", False))
        self.users_treev.heading("2", text="نوع تراکنش",
                                 command=lambda: self.treev_cl_sort("2",
                                                                    False))
        self.users_treev.heading("3", text="مبلغ",
                                 command=lambda: self.treev_cl_sort("3",
                                                                    False))

        self.scrollbar = ttk.Scrollbar(self.fr_treev,
                                       command=self.users_treev.yview,
                                       orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1)
        self.users_treev.configure(xscrollcommand=self.scrollbar.set)

        self.btn_Daryaft = Button(self.fr_edit, text="دریافت وجه",
                                  command=self.daryaft)
        self.btn_Daryaft.grid(row=0, column=0)
        self.btn_Enteghal = Button(self.fr_edit, text="انتقال وجه",
                                   command=self.enteghal)
        self.btn_Enteghal.grid(row=1, column=0, pady=10, padx=10)
        self.btn_Mojoodi = Button(self.fr_edit, text="مشاهده موجودی",
                                  command=self.mojoodi)
        self.btn_Mojoodi.grid(row=2, column=0, ipadx=10)
        self.btn_edit = Button(self.fr_edit, text="ویرایش اطلاعات",
                               command=self.edit, relief=tk.GROOVE)
        self.btn_edit.grid(row=3, column=0, pady=10, ipadx=10)

        for trans in self.list_transaction:
            self.users_treev.insert("", "end", values=trans)

    def daryaft(self):
        children = self.tab_Daryaft.winfo_children()
        if children:  # if a edit_view panel is open then ignore.
            return None
        Daryaft1(self.tab_Daryaft, self.balance, self.callback1,
                 self.close_tab, self.msg_err)
        self.tabs.add(self.tab_Daryaft, text="دریافت وجه")

    def enteghal(self):
        children = self.tab_Enteghal.winfo_children()
        if children != []:  # if a edit_view panel is open then ignore.
            return None
        Enteghal1(self.tab_Enteghal, self.callback2, self.close_tab,
                  self.msg_err)
        self.tabs.add(self.tab_Enteghal, text="انتقال وجه")

    def mojoodi(self):
        children = self.tab_Mojoodi.winfo_children()
        if children:  # if a edit_view panel is open then ignore.
            return None
        Mojoodi1(self.tab_Mojoodi, self.balance, self.close_tab, self.msg_err)
        self.tabs.add(self.tab_Mojoodi, text="موجودی حساب")

    def edit(self):
        children = self.tab_edit.winfo_children()
        if children:  # if a edit_view panel is open then ignore.
            return None
        Edit1(self.username, self.tab_edit, self.callback5, self.close_tab,
              self.msg_err)
        self.tabs.add(self.tab_edit, text="ویرایش اطلاعات")

    def close_tab(self):
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
    min_year = 1900
    max_year = 2020

    start = datetime.date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)

    typetrans = ["انتقال", "برداشت", "دریافت"]
    lst = [(start + (end - start) * random.random(), random.choice(typetrans),
            random.randint(10000, 30000)) for i in range(20)]


    def takeSecond(elem):
        return elem[0]


    lst.sort(key=takeSecond, reverse=True)
    panel = CustomerView("Tabasom", "Puriaee", "1000", lst)
    panel.run()
