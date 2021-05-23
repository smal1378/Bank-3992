from gui_configuration import Button, Frame
import tkinter as tk

class EditView(Frame):
    '''
    this Frame collects new data and send them back to main.py via callback()
    callback1 will close tab after clicking btn submit.
    '''
    
    def __init__(self, name, id_, master = None, callback = None,
                                                 callback1 = None):
        super().__init__(master)
        self.name = name
        self.id_ = id_
        self.callback = callback  # change_employee()
        self.callback1 = callback1  # close_tab()
        self.pack()
        
        # Defining widgets
        self.lbl_name = tk.Label(self, text = "Name:")
        self.lbl_name.grid(row = 0, column = 0)  
        self.lbl_id = tk.Label(self, text = "ID:")
        self.lbl_id.grid(row = 1, column = 0)
        self.lbl_username = tk.Label(self, text = "Username:")
        self.lbl_username.grid(row = 2, column = 0)        
        self.lbl_pass = tk.Label(self, text = "Password:")
        self.lbl_pass.grid(row = 3, column = 0)
        
        self.ent_name = tk.Entry(self)
        self.ent_name.grid(row = 0, column = 1)
        self.ent_id = tk.Entry(self)
        self.ent_id.grid(row = 1, column = 1)
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row = 2, column = 1)
        self.ent_pass = tk.Entry(self)
        self.ent_pass.grid(row = 3, column = 1)
        
        self.btn_submit = Button(self, text = "Submit",
                                    command = self.submit)
        self.btn_submit.grid(row = 4, column = 0, columnspan = 2)
        
        # Preview texts in entry based on self.name and self.id_
        self.ent_name.insert(tk.END, self.name)
        self.ent_id.insert(tk.END, self.id_)
        
    def submit(self):
        data = self.return_data()
        print(data)
        if self.callback:
            self.callback(*data)
            if self.callback1:  # = if datas been sent then close the tab.
                self.callback1()
                
    def return_data(self):
        new_name = self.ent_name.get()
        new_id = self.ent_id.get()
        new_username = self.ent_username.get()
        new_pass = self.ent_pass.get()
        new_data = (self.id_, new_name, new_id, new_username, new_pass)
        if all(item.isalnum() for item in new_data):
            return new_data
        