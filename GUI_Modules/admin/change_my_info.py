import tkinter as tk

from ..gui_configuration import Button, Frame


class ChangeMyInfo(Frame):
    def __init__(self, name, master=None, callback1=None,
                 callback2=None,
                 callback3=None):
        super().__init__(master)
        self.name = name
        self.callback1 = callback1
        self.callback2 = callback2
        self.callback3 = callback3
        self.pack()

        self.lbl_name = tk.Label(self, text="Username:")
        self.lbl_name.grid(row=0, column=0)
        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0)

        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1)
        self.ent_pass = tk.Entry(self, show="*")
        self.ent_pass.grid(row=1, column=1)

        self.btn_submit = Button(self, text="Submit",
                                 command=self.submit)
        self.btn_submit.grid(row=2, column=0, columnspan=2)

        self.ent_username.insert(tk.END, self.name)

    def submit(self):
        data = self.return_data()
        if self.callback1:  # sending data to main.py
            result = self.callback1(*data, self.callback3)
            self.clear()
            if result:
                if self.callback2:  # = if no err occured then close the tab.
                    self.callback2()

    def return_data(self):
        new_username = self.ent_name.get()
        new_pass = self.ent_pass.get()
        new_data = (new_name, new_pass)
        return [data if not data.isspace() and data != "" else None
                for data in new_data]

    def clear(self):
        self.ent_name.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)


if __name__ == "__main__":
    win = tk.Tk()
    fr = ChangeMyInfo("negin_dvz", win)
    win.mainloop()
