class Admin:
    def __init__(self,name):
        self.name=name
        self.all_employees={}
    def del_employees(self,code):
        if code in self.all_employees:
            del self.all_employees[code]
            return 1
        return 2
    def all_employees(self):
        for key , value in self.all_employees:
            yield key, value

    def del_agency(self, code):
        if code in self.all_agencies:
            del self.all_agencies[code]
            return 1    #successful
        return 2    # not in list

    def add_to_agency(self, employee, agency_code):
        if not agency_code in self.all_agencies:
            return 2
        for key in self.all_agencies:
            if employee.ID in self.all_agencies[key].all_employees:
                return 3, key
        self.all_agencies[agency_code].all_employees[employee.ID] = employee
        return 1
    
    def all_employee(self): # generator
        for key, value in self.all_employees:
            yield key, value
    
    def all_agencies(self): # generator
        for key, value in self.all_agencies:
            yield key, value
    
    def all_employees_salary(self):
        total = 0
        for key in self.all_employees:
            total += self.all_employees[key].salary
        return total

from tkinter import *
from tkinter import messagebox
counter=0
def __init__(self,name,callback1=None,callback2=None,callback3=None,callback4=None,callback5=None
             ,callback6=None,callback7=None,callback8=None):
    
    self.name=name
    self.all_employees={}
    self.callback1=callback1
    self.callback2=callbck2
    self.callback3=callback3
    self.callback4=callback4
    self.callback5=callback5
    self.callback6=callback6
    self.callback7=callback7
    self.callback8=callback8

    
def del_employees(self,code):
    if code in self.all_employees:
        del self.all_employees[code]
        return 1
    return 2
def all_employees(self):
    for key , value in self.all_employees:
        yield key, value

def del_agency(self, code):
    if code in self.all_agencies:
        del self.all_agencies[code]
        return 1    #successful
    return 2    # not in list

def add_to_agency(self, employee, agency_code):
    def insert_element():
        
        list_box.insert(END,name_entry.get())


    def clear_box():    
        list_box.delete(0,END)


    name_entry = Entry(window)
    name_entry.pack()


    send_btn = Button(window,text="send to box",command=insert_element)
    send_btn.pack()


    send_btn = Button(window,text="clear the box",command=clear_box)
    send_btn.pack()


    list_box = Listbox(window)
    list_box.pack()
    
def all_employee(self): # generator
    for key, value in self.all_employees:
        yield key, value
    
def all_agencies(self): # generator
    for key, value in self.all_agencies:
        yield key, value
    
def all_employees_salary(self):
    total = 0
    for key in self.all_employees:
        total += self.all_employees[key].salary
    return total

window=Tk()
window.title("final projekt")
window.minsize(400,300)
scrollbar= Scrollbar(window)
scrollbar.pack(side = RIGHT , fill = BOTH)

#btn1=Button(window,text="del_employee" , font=("Tahoma" , 20) , fg="brown",command=del_employees).pack()
#btn2=Button(window , text =" all_employees " , font=("Tahoma "  ,20) ,fg="green" , command=all_employees).pack()
#btn3=Button(window , text="del_agency" , font=("Tahoma" , 20 ) , fg ="brown" , background="aqua",command=del_agency).pack()
#btn4=Button(window , text =" add_to_ageny " , font=("Tahoma "  ,20) ,fg="green",command=add_to_agency).pack()
#label5=Label(window , text =" all_employees " , font=("Tahoma "  ,20) ,fg="green").pack()
#btn6=Button(window , text =" all_agencies " , font=("Tahoma "  ,20) ,fg="green", command=all_agencies).pack()

#btn7=Button(window , text =" all_employees_salary " , font=("Tahoma "  ,20) ,fg="green", command=all_employees_salary).pack()
menubar=Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="delete employees", command=del_employees)
filemenu.add_command(label="list of employees ", command=all_employees)
filemenu.add_command(label="all employees salary", command=all_employees_salary)
filemenu.add_separator()


filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="employees", menu=filemenu)
menubar2=Menu(window)
filemenu2 = Menu(menubar2 , tearoff= 0)
filemenu2.add_command(label="delete agency", command=del_agency)
filemenu2.add_command(label="add agency", command=add_to_agency)
filemenu2.add_command(label="list of  agencies", command=all_agencies)

menubar.add_cascade(label="agency", menu=filemenu2)

filemenu2.add_separator()


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)


window .config(menu=menubar)






lbl=Label(window,text="add agency",fg="purple").pack()

def insert_element():
    list_box.insert(END,name_entry.get())


def clear_box():    
    list_box.delete(0,END)


name_entry = Entry(window)
name_entry.pack()

send_btn = Button(window,text="send to box",command=insert_element)
send_btn.pack()


send_btn = Button(window,text="clear the box",command=clear_box)
send_btn.pack()


list_box = Listbox(window)
list_box.pack()



window.geometry("300x300")
window.mainloop()






























    

    
