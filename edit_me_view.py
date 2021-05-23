from gui_configuration import Button, Frame
import tkinter as tk

class EditMeView(Frame):
    '''
    this Frame collects new data and send them back to main.py via callback()
    callback1 will close tab after clicking btn submit.
    '''
    
    def __init__(self, username, master = None, callback = None,
                                                callback1 = None):
        super().__init__(master)
        self.username = username
        self.callback = callback  # set_my_info()
        self.callback1 = callback1  # close_tab()
        self.pack()
        
        # Defining widgets
        self.lbl_username = tk.Label(self, text = "Username:")
        self.lbl_username.grid(row = 0, column = 0)        
        self.lbl_pass = tk.Label(self, text = "Password:")
        self.lbl_pass.grid(row = 1, column = 0)
        
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row = 0, column = 1)
        self.ent_pass = tk.Entry(self)
        self.ent_pass.grid(row = 1, column = 1)
        
        self.btn_submit = Button(self, text = "Submit",
                                    command = self.submit)
        self.btn_submit.grid(row = 2, column = 0, columnspan = 2)
        
        # Preview texts in entry based on self.username
        self.ent_username.insert(tk.END, self.username)

    def submit(self):
        data = self.return_data()
        print(data)
        if self.callback:
            self.callback(*data)
            if self.callback1:  # = if datas been sent then close the tab.
                self.callback1()
    def return_data(self):
        new_username = self.ent_username.get()
        new_pass = self.ent_pass.get()
        new_data = (new_username, new_pass)
        if all(item.isalnum() for item in new_data):  # not so sure :/
            return new_data
        