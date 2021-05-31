from gui_configuration import Button, Frame
import tkinter as tk

class EditManager(Frame):
    
    
    def __init__(self, name, username, master = None, callback1= None,
                                                 callback2 = None,
                                                 callback3 = None):
        super().__init__(master)
        self.name = name
        self.username = username
        self.callback3 = callback3
        self.callback1 = callback1  
        self.callback2 = callback2  
        self.pack()
        
        
        self.lbl_name = tk.Label(self, text = "Name:")
        self.lbl_name.grid(row = 0, column = 0)  
        self.lbl_username = tk.Label(self, text = "Username:")
        self.lbl_username.grid(row = 2, column = 0)        
        self.lbl_pass = tk.Label(self, text = "Password:")
        self.lbl_pass.grid(row = 4, column = 0)
        self.lbl_id = tk.Label(self, text = "ID:")
        self.lbl_id.grid(row = 6, column = 0)
        
        self.ent_name = tk.Entry(self)
        self.ent_name.grid(row = 0, column = 1)
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row = 2, column = 1)
        self.ent_pass = tk.Entry(self, show = "*")
        self.ent_pass.grid(row = 4, column = 1)
        self.ent_id = tk.Entry(self)
        self.ent_id.grid(row = 6, column = 1)
        
        self.btn_submit = Button(self, text = "change",
                                    command = self.change)
        self.btn_submit.grid(row = 8, column = 0, columnspan = 2)

        self.btn_new = Button(self, text = "new",
                                    command = self.new_manager)
        self.btn_new.grid(row = 10, column = 0, columnspan =2)


        self.btn_new = Button(self, text = "delete",
                                    command = self.del_manager)
        self.btn_new.grid(row = 12, column = 0, columnspan =2)
        

        self.ent_name.insert(tk.END, self.name)
        self.ent_username.insert(tk.END, self.username)


        
    def new_manager(self, branch , branch_ID):
        
        new_name = self.ent_name.get()
        new_id = self.ent_id.get()
        new_username = self.ent_username.get()
        new_pass = self.ent_pass.get()
        new_data = (self.old_user, new_username, new_id, new_pass, new_name)
        return [data if not data.isspace() and data != "" else None
               for data in new_data]

        
    def del_manager(self, code):
        if ID in self.all_branch:
            del self.all_branch[code]
            return 1    #successful
        return 2    # not in list
    
        
    def change(self):
        data = self.new_branch()
        if self.callback:  
            result = self.callback(*data, self.callback3)
            self.clear()
            if result:
                if self.callback2:  
                    self.callback2()
                

        
    def clear(self):
        self.ent_name.delete(0, tk.END)
        self.ent_username.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)
        self.ent_id.delete(0, tk.END)
        
if __name__ == "__main__":
    win = tk.Tk()
    fr = EditManager("negin", "negin_dvz", win)
    win.mainloop()
    
