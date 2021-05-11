import tkinter as tk
from tkinter import ttk
import random  # just for card number

Default_Theme = "white"

class Client:  
    def __init__(self, name, username, password, _id):
        self.name = name
        self.username = username
        self.password = password
        self._id = _id
        self.card_num = random.randint(10**16, (10**17)-1)
        self.balance = 0
    

class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg=Default_Theme)

class Toplevel(tk.Toplevel):
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        super().__init__(master, **kwargs)
        
class Depositview(tk.Toplevel):
    def __init__(self, user, master = None):
        super().__init__(master)
        self.user = user
        self.geometry("200x200")
        self.lblinfo = tk.Label(self, text = f"deposit view for {user.name}")
        self.lblinfo.pack()
        self.transient()
        
class WithdrawalView(tk.Toplevel):  
    def __init__(self, user, master = None):
        super().__init__(master)
        self.user = user
        self.geometry("200x200")
        self.lblinfo = tk.Label(self, text = f"withdrawal view for {user.name}")
        self.lblinfo.pack()
        self.transient()
 
class UserView(tk.Toplevel):
    def __init__(self, user, master = None):
        super().__init__(master) 
        self.geometry("300x200")
        self.user = user
        self.title(f"Panel user for {user.name}")
        self.btn_deposit = tk.Button(self, text = "Deposit into account",
                                     command = lambda: Depositview(user, self))
        self.btn_deposit.pack()
        self.btn_withdrawal = tk.Button(self, text = "withdrawal from account",
                                        command = lambda: WithdrawalView(user, self))
        self.btn_withdrawal.pack()
 
class EmployeeView(tk.Toplevel):
    def __init__(self, dict_users, master = None):
        super().__init__(master)
        self.dict_users = dict_users
        
        self.users_list = ttk.Treeview(self, selectmode = 'browse')
        self.users_list.pack(side = "right")
        
        self.scrollbar = ttk.Scrollbar(self, command = self.users_list.yview, 
                                      orient = tk.VERTICAL)
        self.scrollbar.pack(side = "right", fill = "x")
        
        self.users_list.configure(xscrollcommand = self.scrollbar.set)
        self.users_list['columns'] = ("1", "2", "3", "4")  
        self.users_list["show"] = "headings"
        self.users_list.column("1", width = 90, anchor ='c')
        self.users_list.column("2", width = 90, anchor ='c')
        self.users_list.column("3", width = 90, anchor ='c')
        self.users_list.column("4", width = 90, anchor ='c')
        self.users_list.heading("1", text ="Name")
        self.users_list.heading("2", text ="Username")
        self.users_list.heading("3", text ="ID")
        self.users_list.heading("4", text = "Card number")
        
        for user in self.dict_users.values():
            self.users_list.insert("", "end",
                                   values = (user.name, user.username,
                                             user._id, user.card_num))
        self.users_list.bind("<Double-1>", self.onDoubleClick)
    def onDoubleClick(self, event):
        user = self.users_list.selection()
        username = self.users_list.item(user)["values"][1]  # values\str(username)
        UserView(self.dict_users.get(username), self)
        
        
    
    
        
    
win = tk.Tk()
win.iconify()
lst = {f"username{i}": Client(f"user {i+1}", f"username{i}", i*2+1, i**2) for i in range(50)}
panel = EmployeeView(lst, win)

win.mainloop()
   

    

        