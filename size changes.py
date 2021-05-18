import tkinter as tk 
from tkinter import ttk
import random  # just for card number

Default_Theme = "red"

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
        
class DepositView(tk.Toplevel):
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
                                     command = lambda: DepositView(user, self))
        self.btn_deposit.pack()
        self.btn_withdrawal = tk.Button(self, text = "withdrawal from account",
                                        command = lambda: WithdrawalView(user, self))
        self.btn_withdrawal.pack()
 
class ManagerView(tk.Toplevel):
    
    def __init__(self, manager_obj, dict_users, master = None):
        super().__init__(master)
        self.dict_users = dict_users
        self.title(f"Panel manager: {manager_obj.name}")
        self.screen_height = self.winfo_screenheight()
        self.screeen_width = self.winfo_screenwidth()
        self.geometry(f"880x400+{int(self.screeen_width / 2) - 440}+\
{int(self.screen_height / 2) - 200}")
        #self.icon
        #self.resizable
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row = 0, column = 0)
        
        self.fr_tab_main = tk.Frame(self)  # sorry for long names :/
        self.fr_tab_main.grid(row = 0, column = 0)
        self.fr_tab_edit_me = tk.Frame(self)
        self.fr_tab_edit_me.grid(row = 0, column = 0)
        self.fr_tab_add_user = tk.Frame(self)
        self.fr_tab_add_user.grid(row = 0, column = 0)
        self.fr_tab_edit_user = tk.Frame(self)
        self.fr_tab_edit_user.grid(row = 0, column = 0)        
        self.tabs.add(self.fr_tab_main, text = "Main menu") # main entrance
        
        # Defining main-tab frames
        self.fr_about = tk.LabelFrame(self.fr_tab_main, text = "About me")
        self.fr_about.grid(row = 0, column = 0, rowspan = 2, padx = 10)
        self.fr_seachbar = tk.Frame(self.fr_tab_main)
        self.fr_seachbar.grid(row = 0, column = 1)
        self.fr_list = tk.Frame(self.fr_tab_main)
        self.fr_list.grid(row = 1, column = 1)
        self.fr_edit_user = tk.Frame(self.fr_tab_main)
        self.fr_edit_user.grid(row = 1, column = 2)
        
        # Frame about
        self.lbl_name = tk.Label(self.fr_about, text = "Name:")
        self.lbl_name.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 5)
        self.lbl_name = tk.Label(self.fr_about, text = manager_obj.name)
        self.lbl_name.grid(row = 0, column = 1, sticky = "w", padx = 10, pady = 5)
        self.lbl_username = tk.Label(self.fr_about, text = "Username:")
        self.lbl_username.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 5)
        self.lbl_username = tk.Label(self.fr_about, text = manager_obj.username)
        self.lbl_username.grid(row = 1, column = 1, sticky = "w", padx = 10, pady = 5)
        self.lbl_passworld = tk.Label(self.fr_about, text = "Password:")
        self.lbl_passworld.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 5)
        self.lbl_passworld = tk.Label(self.fr_about, text = manager_obj.password)
        self.lbl_passworld.grid(row = 2, column = 1, sticky = "w", padx = 10, pady = 5)
        self.lbl_id_ = tk.Label(self.fr_about, text = "ID:")
        self.lbl_id_.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 5)
        self.lbl_id_ = tk.Label(self.fr_about, text = manager_obj._id)
        self.lbl_id_.grid(row = 3, column = 1, sticky = "w", padx = 10, pady = 5)
        self.btn_edit_me = tk.Button(self.fr_about, text = "Edit",
                                     command = self.edit_me, width = 10, 
                                     relief = tk.GROOVE)
        self.btn_edit_me.grid(row = 4, column = 0, columnspan = 2, pady = 5)    
        
        # Frame search bar
        self.search_bar = tk.Entry(self.fr_seachbar, width = 49)
        self.search_bar.grid(row = 0, column = 0, pady = 10)
        self.btn_search = tk.Button(self.fr_seachbar, text = "search", 
                                    command = self.search_treev, width = 10)
        self.btn_search.grid(row = 0, column = 1, padx = 5)
        self.btn_refresh = tk.Button(self.fr_seachbar, text = "Refresh", 
                                     command = self.refresh_treev, width = 10)
        self.btn_refresh.grid(row = 0, column = 2)
        
        # Frame list
        self.users_treev = ttk.Treeview(self.fr_list, selectmode = 'browse', height = 15)
        self.users_treev.grid(row = 0, column = 0)
        self.users_treev['columns'] = ("1", "2", "3", "4")  
        self.users_treev["show"] = "headings"
        self.numeric_columns = ("3", "4") # conn: sort function
        self.users_treev.column("1", width = 140, anchor ='c')
        self.users_treev.column("2", width = 140, anchor ='c')
        self.users_treev.column("3", width = 140, anchor ='c')
        self.users_treev.column("4", width = 140, anchor ='c')
        self.users_treev.heading("1", text ="Name",
                                 command = lambda: self.treev_cl_sort("1", False))
        self.users_treev.heading("2", text ="Username",
                                 command = lambda: self.treev_cl_sort("2", False))
        self.users_treev.heading("3", text ="ID",
                                 command = lambda: self.treev_cl_sort("3", False))
        self.users_treev.heading("4", text = "Card number",
                                 command = lambda: self.treev_cl_sort("4", False))
        self.scrollbar = ttk.Scrollbar(self.fr_list, command = self.users_treev.yview, 
                                      orient = tk.VERTICAL)
        self.scrollbar.grid(row = 0, column = 1)
        self.users_treev.configure(xscrollcommand = self.scrollbar.set)
        
        # Frame edit user
        self.btn_add_user = tk.Button(self.fr_edit_user, text = "Add user",
                                      command = self.add_user, width = 10)
        self.btn_add_user.grid(row = 0, column = 0)
        self.btn_edit_user = tk.Button(self.fr_edit_user, text = "Edit user",
                                       command = self.edit_user, width = 10)
        self.btn_edit_user.grid(row = 1, column = 0, pady = 10, padx = 10)
        self.btn_delete_user = tk.Button(self.fr_edit_user,
                                         text = "Delete user",
                                         command = self.del_user, width = 10)
        self.btn_delete_user.grid(row = 2, column = 0)
        
        for user in self.dict_users.values():
            self.users_treev.insert("", "end",
                                   values = (user.name, user.username,
                                             user._id, user.card_num))
        self.users_treev.bind("<Double-1>", self.onDoubleClick)
        
    def onDoubleClick(self, event): # double click on treev to open users panel
        user = self.users_treev.selection()
        if user == ():# if double clicked on headings or any other empty space
            return None
        username = self.users_treev.item(user)["values"][1]  # values\str(username)
        UserView(self.dict_users.get(username), self)
        self.users_treev.selection_remove(user[0]) # clear selections here
        
    def edit_me(self):
        self.lbl_info = tk.Label(self.fr_tab_edit_me,
                                  text = "Edit me menu will appear here")
        self.lbl_info.grid(row = 0, column = 0)
        self.btn_submit = tk.Button(self.fr_tab_edit_me,
                                    text = "test submit btn",
                                    command = lambda: self.tabs.forget(self.tabs.select()))
        self.btn_submit.grid(row = 0, column = 1)
        self.tabs.add(self.fr_tab_edit_me, text = "Edit-me menu")
        
    def add_user(self):
        # open a menu to add user
        # getting data and savind in dict_users and apply changes to treeview
        self.lbl_info = tk.Label(self.fr_tab_add_user,
                                 text = "add user menu will appear here")
        self.lbl_info.grid(row = 0, column = 0)
        self.btn_submit = tk.Button(self.fr_tab_add_user,
                                    text = "test submit btn",
                                    command = lambda: self.tabs.forget(self.tabs.select()))
        self.btn_submit.grid(row = 0, column = 1)
        self.tabs.add(self.fr_tab_add_user, text = "Add-user menu")
        
    def del_user(self):
        selected = self.users_treev.focus()  # returns selected item ID
        if selected == "":
            return 
        data = self.users_treev.item(selected, "values") # (name, user, ...)
        del self.dict_users[data[1]] # cause dict keys are username for now
        self.users_treev.delete(selected)
        # send information to main.py 
        print(self.dict_users.keys())  # just a test
        
    def edit_user(self):
        selected = self.users_treev.focus()
        if selected == "":
            return 
        data = self.users_treev.item(selected, "values")
        user_obj = self.dict_users[data[1]]
        # send obj to edit menu
        # get new obj and update dict_users
        # update treeview        
        # send information to main.py
        self.lbl_info = tk.Label(self.fr_tab_edit_user,
                                 text = "edit user menu will appear here")
        self.lbl_info.grid(row = 0, column = 0)
        self.btn_submit = tk.Button(self.fr_tab_edit_user,
                                    text = "test submit btn",
                                    command = lambda: self.tabs.forget(self.tabs.select()))
        self.btn_submit.grid(row = 0, column = 1)
        self.tabs.add(self.fr_tab_edit_user, text = "Edit-user menu")
        self.users_treev.selection_remove(selected) # clear selections here
        
    def refresh_treev(self):
        self.users_treev.delete(*self.users_treev.get_children())
        for user in self.dict_users.values():
            self.users_treev.insert("", "end",
                                   values = (user.name, user.username,
                                             user._id, user.card_num))
        
    def search_treev(self): # key could be anything
        search_key = self.search_bar.get()
        all_items = []
        for child in self.users_treev.get_children():
            all_items.append(self.users_treev.item(child, "values"))
        matched_items = []
        for item in all_items:
            if search_key in item:
                matched_items.append(item)
        if len(matched_items) > 0:
            self.users_treev.delete(*self.users_treev.get_children())
            for item in matched_items:
                self.users_treev.insert("", "end",
                                        values = item)
        else:
            print("nothing found") # test
            # better to use messegebox.showalert     
    def treev_cl_sort(self, col, reverse):  # does work too good. ignore for now
        if col in self.numeric_columns:
            users = [(int(self.users_treev.set(id_, col)), id_) \
                 for id_ in self.users_treev.get_children()]
        else:
            users = [(self.users_treev.set(id_, col), id_) \
                 for id_ in self.users_treev.get_children()]
        users.sort(reverse = reverse)
        for index, (val, id_) in enumerate(users):
            self.users_treev.move(id_, '', index)
        self.users_treev.heading(col, command=lambda: \
               self.treev_cl_sort(col, not reverse))
    
win = Tk()

lst = {f"username{i + 1}": Client(f"user {i+1}", f"username{i + 1}", i*2+1, i**2) for i in range(20)}
manager = Client("siamak", "siamak_sdi", 12345, 2190245001)
panel = ManagerView(manager, lst, win)

win.mainloop()        