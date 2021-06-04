from gui_configuration import Button, Frame
import tkinter as tk  # for test (win = tk.TK())
from tkinter import ttk  # for treeview

class Accounts_view(Frame):
    
    def __init__(self, id_, master = None, callback = None, callback1 = None,
                                          callback2 = None, callback3 = None):
        super().__init__(master)
        self.id_ = id_
        self.callback = callback  # add_account()
        self.callback1 = callback1  # get_accounts()
        self.callback2 = callback2  # remove_account()
        self.callback3 = callback3  # add_money()
        self.pack()
        
        # Defining main frames
        self.fr_buttons = Frame(self)
        self.fr_buttons.grid(row = 0, column = 0)
        self.fr_treeview = Frame(self)
        self.fr_treeview.grid(row = 0, column = 1)
        
        # Frame Buttons
        self.btn_add_acc = Button(self.fr_buttons, text = "add account", 
                                  command = self.add_account)
        self.btn_add_acc.grid(row = 0, column = 0)
        self.btn_del_acc = Button(self.fr_buttons, text = "delete account", 
                                  command = self.del_account)
        self.btn_del_acc.grid(row = 1, column = 0)
        self.btn_add_money = Button(self.fr_buttons, text = "add money", 
                                  command = self.add_money)
        self.btn_add_money.grid(row = 2, column = 0)
        
        # Frame Treev
        
        self.treev = ttk.Treeview(self.fr_treeview, selectmode = "browse",
                                  height = 15)
        self.treev.grid(row = 0, column = 0)
        self.treev['columns'] = ("1", "2")
        self.treev["show"] = "headings"
        self.treev.column("1", width = 140, anchor ='c')
        self.treev.column("2", width = 140, anchor ='c')
        self.treev.heading("1", text = "account number")
        self.treev.heading("2", text = "remaining")
        self.scrollbar = ttk.Scrollbar(self.fr_treeview,
                                       command = self.treev.yview, 
                                       orient = tk.VERTICAL)
        self.scrollbar.grid(row = 0, column = 1)
        self.treev.configure(xscrollcommand = self.scrollbar.set)
        
        if self.callback1:  # filling treeview 
            for data in self.callback1():
                self.treev.insert("", "end", values = data)
                
        
    def add_money(self):
        selected = self.treev.selection()
        if selected == ():
            return None
        acc_num, remaining = self.treev.item(selected, "values")
        if self.callback3:
            self.callback3(acc_num)
            
    def del_account(self):
        selected = self.treev.selection()
        if selected == ():
            return None
        acc_num, remaining = self.treev.item(selected, "values")
        self.treev.delete(selected)
        if self.callback2:
            self.callback2(acc_num)
            
    def add_account(self):
        if self.callback:
            card_num = self.callback(self.id_)
            self.treev.insert("", "end", values = (card_num, "0"))
            
if __name__ == "__main__":
    
    def test():
        return [("541654165416", "12000"),
                ("646623624652", "85000"),
                ("542364242848", "99000"),
                ("516516512899", "30000"),]
    
    win = tk.Tk()
    test = Accounts_view(15, win, None, test)
    win.mainloop()
     