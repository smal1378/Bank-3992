from gui_configuration import Button , Frame
import tkinter as tk

class ShowAll(Frame):

    def __init__ (self,master=None , callback1 = None , callback2= None , callback3=None
                  ,):
        super().__init__(master)
        self.callback1=callback1
        self.callback2=callback2
        self.callback3=callback3
        self.all_employees_salary={}
        self.all_manager={}
        self.customer={}
        
        self.pack()


        self.btn_all = Button(self, text = "show all manager",font=("Tahoma",12),
                                    command = self.all_manager)
        self.btn_all.grid(row = 4, column = 0, columnspan = 4)

        self.btn_all = Button(self, text = "show all customer",font=("Tahoma",12),
                                    command = self.all_customer)
        self.btn_all.grid(row = 6, column = 0, columnspan = 4)

        
        self.btn_all = Button(self, text = "show all employee salary",font=("Tahoma",12)
                                    ,command = self.all_employees_salary)
        self.btn_all.grid(row = 8, column = 0, columnspan = 4)

        
    def all_employee(self): # generator
        for key, value in self.all_employees:
            yield key, value
    
    def all_manager(self): # generator
        for key, value in self.all_manager:
            yield key, value
    def all_customer(self): # generator
        for key, value in self.all_customer:
            yield key, value
    def all_employees_salary(self):
        total = 0
        for key in self.all_employees:
            total += self.all_employees[key].salary
        return total
    
if __name__ == "__main__":
    win=tk.Tk()
    fr=ShowAll(win)
    win.mainloop()
        
