from tkinter import *
import tkinter as tk
from tkinter import ttk
from manager1 import EditManager
from gui_configuration import Tk, Frame
from branch import EditBranch
from change_my_info import Change_my_info
class AdminView(Tk):
    
    def __init__(self, username, lst_manager, lst_branch,
                 callback1 = None, callback2 = None, 
                 callback3 = None, callback4 = None, 
                 callback5 = None, callback6 = None, 
                 callback7 = None, callback8 = None, 
                 callback9 = None, callback10 = None,
                 callback11 = None):
        super().__init__()
        self.username = username
        self.lst_manager = lst_manager
        self.lst_branch = lst_branch
        
        # callbacks:
        self.callback1 = callback1  # change_admin_info()
        self.callback2 = callback2  # new_branch()
        self.callback3 = callback3  # del_branch()
        self.callback4 = callback4  # change_branch()
        self.callback5 = callback5  # all_employees()
        self.callback6 = callback6  # all_customers()
        self.callback7 = callback7  # all_managers()
        self.callback8 = callback8  # new_manager()
        self.callback9 = callback9  # set_manager()
        self.callback10 = callback10  # change_manager()
        self.callback11 = callback11  # del_manager()
        
        self.title = f"Panel Admin: {self.username}" 
        self.tabs = ttk.Notebook(self)
        self.tabs.grid(row = 0, column = 0)
        
        # Defining tabs
        self.tab_main = Frame(self)
        self.tab_main.grid(row = 0, column = 0)
        self.tab_managers = Frame(self)
        self.tab_managers.grid(row = 0, column = 0)
        self.tab_employees = Frame(self)
        self.tab_employees.grid(row = 0, column = 0)
        self.tab_customers = Frame(self)
        self.tab_customers.grid(row = 0, column = 0)
        self.tab_branches = Frame(self)
        self.tab_branches.grid(row = 0, column = 0)
        self.tabs.add(self.tab_main, text = "Main")
        
        # Defining "tab Main" frames
        self.fr_side = Frame(self.tab_main)
        self.fr_side.grid(row = 0, column = 0)
        self.fr_details = Frame(self.tab_main)
        self.fr_details.grid(row = 0, column = 1)
        
        # Frame side
        self.lbl_manager = tk.Label(self.fr_side, text = "Managers:")
        self.lbl_manager.grid(row = 18, column = 1, padx = 10, pady = 10)        
        self.lbl_mng_num = tk.Button(self.fr_side, text = "not set yet",command= self.open_managers)
        self.lbl_mng_num.grid(row = 18, column = 2, padx = 10, pady = 10)
        
        self.lbl_employees = tk.Label(self.fr_side, text = "Employees:")
        self.lbl_employees.grid(row = 16, column = 1, padx = 10, pady = 10)     
        self.lbl_emp_num = tk.Button(self.fr_side, text = "not set yet" , command=self.open_employees)
        self.lbl_emp_num.grid(row = 16, column = 2, padx = 10, pady = 10)   
        
        self.lbl_customers = tk.Label(self.fr_side, text = "Customers:")
        self.lbl_customers.grid(row =14, column= 1, padx = 10, pady = 10)     
        self.lbl_ct_num = tk.Button(self.fr_side, text = "not set yet" , command= self.open_customers)
        self.lbl_ct_num.grid(row = 14, column = 2, padx = 10, pady = 10)
        
        self.lbl_branches = tk.Label(self.fr_side, text = "Branches: ")
        self.lbl_branches.grid(row = 20, column = 1, padx = 10, pady = 10)
        self.lbl_br_num = tk.Button(self.fr_side, text = "not set yet" , command= self.open_branches)
        self.lbl_br_num.grid(row = 20, column = 2, padx = 10, pady = 10)
        
        self.lbl_mng_num.bind("<Double-1>", self.open_managers)
        self.lbl_emp_num.bind("<Double-1>", self.open_employees)
        self.lbl_ct_num.bind("<Double-1>", self.open_customers)
        self.lbl_br_num.bind("<Double-1>", self.open_branches)
        
        
        
        # Frame details:
        self.lf_now = tk.LabelFrame(self.fr_details, text = "This month")
        self.lf_now.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.lf_past = tk.LabelFrame(self.fr_details, text = "Last month")
        self.lf_past.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.lbl_tf = tk.Label(self.lf_now, text = "Transfer income")
        self.lbl_tf.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.amount_tf = tk.Label(self.lf_now, text = "not set yet")
        self.amount_tf.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.lbl_acc_prof = tk.Label(self.lf_now, text = "Accounts")
        self.lbl_acc_prof.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.amount_acc_prof = tk.Label(self.lf_now, text = "not set yet")
        self.amount_acc_prof.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.lbl_salaries = tk.Label(self.lf_now, text = "Salaries")
        self.lbl_salaries.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.amount_salaries = tk.Label(self.lf_now, text = "not set yet")
        self.amount_salaries.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        self.lbl_income = tk.Label(self.lf_now, text = "Gross profit")
        self.lbl_income.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.amount_income = tk.Label(self.lf_now, text = "not set yet")
        self.amount_income.grid(row = 1, column = 3, padx = 10, pady = 10)
        
        self.lbl_netp = tk.Label(self.lf_now, text = "Net profit")
        self.lbl_netp.grid(row = 0, column = 4, padx = 10, pady = 10)
        self.amount_netp = tk.Label(self.lf_now, text = "not set yet")
        self.amount_netp.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        ####
        
        self.lbl_tf_last = tk.Label(self.lf_past, text = "Transfer income")
        self.lbl_tf_last.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.amount_tf_last = tk.Label(self.lf_past, text = "not set yet")
        self.amount_tf_last.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.lbl_acc_prof_last = tk.Label(self.lf_past, text = "Accounts")
        self.lbl_acc_prof_last.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.amount_acc_prof_last = tk.Label(self.lf_past, text = "not set yet")
        self.amount_acc_prof_last.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        self.lbl_salaries_last = tk.Label(self.lf_past, text = "Salaries")
        self.lbl_salaries_last.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.amount_salaries_last = tk.Label(self.lf_past, text = "not set yet")
        self.amount_salaries_last.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        self.lbl_income_last = tk.Label(self.lf_past, text = "Gross profit")
        self.lbl_income_last.grid(row = 0, column = 3, padx = 10, pady = 10)
        self.amount_income_last = tk.Label(self.lf_past, text = "not set yet")
        self.amount_income_last.grid(row = 1, column = 3, padx = 10, pady = 10)
        
        self.lbl_netp_last = tk.Label(self.lf_past, text = "Net profit")
        self.lbl_netp_last.grid(row = 0, column = 4, padx = 10, pady = 10)
        self.amount_netp_last = tk.Label(self.lf_past, text = "not set yet")
        self.amount_netp_last.grid(row = 1, column = 4, padx = 10, pady = 10)

        
        self.fr_aboutme = tk.LabelFrame(self.tab_main, text = "About me",
                                        bg = "gray")
        self.fr_aboutme.grid(row = 11, column = 0, rowspan = 2, padx = 10)
       
        self.lbl_name = tk.Label(self.fr_aboutme, text = self.username)
        self.lbl_name.grid(row = 12, column = 1,
                           sticky = "w", padx = 10, pady = 5)
        self.lbl_username = tk.Label(self.fr_aboutme, text = "Username:")
        self.lbl_username.grid(row = 12, column = 0,
                               sticky = "w", padx = 10, pady = 5)
        self.lbl_username = tk.Label(self.fr_aboutme, text = self.username)
        self.lbl_username.grid(row = 12, column = 1,
                               sticky = "w", padx = 10, pady = 5)
        self.btn_edit_me = Button(self.fr_aboutme, text = "Edit",
                                  command = self.change_my_info, 
                                  relief = tk.GROOVE)
        self.btn_edit_me.grid(row = 2, column = 0, columnspan = 2, pady = 5)    
        


        ###
        #self.btn_showall = Button(self.fr_showall, text = "show all",command = self.showall)
        #self.btn_showall.grid(row = 2, column = 0)
        

        


    def open_managers(self):
        a=self.tabs.add(self.tab_managers , text="Managers")


        if a!=[]:
            return None
       
        panel=EditManager(self.tab_open_managers,self.callback10,
                          self.close_tab , self.msg_err)
        self.tabs.add(self.tab_open_managers, text = "Managers")

        print("managers opened")
    def open_employees(self):
        
        self.tabs.add(self.tab_employees, text = "Employees")
        print("employees opened")
    def open_customers(self):
        self.tabs.add(self.tab_customers, text = "Customers")
        print("customers opened")
    def open_branches(self , ):
        a=self.tabs.add(self.tab_branches , text="Branches")
        if a!=[]:
            return None
       
        panel=EditBranch(self.tab_open_branches , self.callback3,
                          self.close_tab , self.msg_err)
        self.tabs.add(self.tab_branches, text = "Branches")
        print("branches opened")
    def change_my_info(self):
        b=self.tab_change_my_info.winfo_b()
        if b != [] :
            return None
        panel=Change_my_info(self.username, self.tab_change_my_info , self.callback1,
                             self.close_tab , self.msg_err)
        self.tabs.add(self.tab_change_my_info, text = "Edit-me menu")

        
    
        
        
        
    
    def run(self):
        self.mainloop()
    def close(self):
        self.destroy()
        
    def msg_err(self, title = None, msg = None, master = None):
        if master is None:
            master = self
        tk.messagebox.showerror(title, msg, parent = master)
        
if __name__ == "__main__":
    panel = AdminView("negin_dvz", "negin", [])     
    panel.run()
        
        
        
        
        
        
        
        
        
        
