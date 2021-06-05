from ..gui_configuration import Label, Button
from tkinter import Tk, Entry, Toplevel, W


class LoginView(Tk):
    def __init__(self, callback1):
        super(LoginView, self).__init__()
        self.callback1 = callback1
        self.un_lbl = Label(self, text="Username")
        self.un_lbl.grid()
        self.un_entry = Entry(self)
        self.un_entry.grid(row=0, column=1, sticky=W)
        self.pw_lbl = Label(self, text="Password")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_entry = Entry(self, show="*")
        self.pw_entry.grid(row=1, column=1, sticky=W)
        self.submit_btn = Button(self, text="LOGIN", command=self.reveal)
        self.submit_btn.grid(row=2, column=1, sticky=W)
        self.title("Login")
        self.geometry("250x100")
        self.status = ""

    def show_error(self, message: str):
        self.status = message
        self.window()

    def window(self):
        t = Toplevel(self)
        t.wm_title("Status")
        lab = Label(t, text=self.status)
        lab.pack(side="top", fill="both", expand=False, padx=50, pady=50)

    def reveal(self):
        user = self.un_entry.get()
        password = self.pw_entry.get()
        self.callback1(user, password)


# old:
"""
class LoginView:
    def __init__(self, callback1):
        self.callback1 = callback1

    def mainloop(self):
        user = input("username: ")
        password = input("password: ")
        self.callback1(user, password)

    def destroy(self):
        pass

    @staticmethod
    def show_error(message: str = "Error"):
        print(message)
"""