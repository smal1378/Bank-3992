import tkinter as tk
from ..gui_configuration import Button, Frame, Label


class Edit1(Frame):

    def __init__(self, username, master=None, callback=None,callback1=None,callback2=None):
        super().__init__(master)
        self.username = username
        self.callback = callback
        self.callback1 = callback1
        self.callback2 = callback2
        self.pack(expand=True)

        self.lbl_username.grid(row=0, column=0,padx=10, pady=10, sticky="w")
        self.lbl_pass = Label(self, text="رمز عبور:")
        self.lbl_pass.grid(row=1, column=0,padx=10, pady=10, sticky="w")

        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1)
        self.ent_pass = tk.Entry(self, show="*")
        self.ent_pass.grid(row=1, column=1)

        self.btn_submit = Button(self, text="تایید",command=self.submit)
        self.btn_submit.grid(row=2, column=0, columnspan=2,padx=10, pady=10)

        self.ent_username.insert(tk.END, self.username)
        self.ent_username.focus_set()

        self.entries = [ent for ent in self.winfo_children() if isinstance(ent, tk.Entry)]
        self.ent_username.bind("<Return>", lambda _: self.entries[1].focus_set())
        self.ent_pass.bind("<Return>", lambda _: self.btn_submit.invoke())

    def submit(self):
        data = self.return_data()
        if self.callback:
            result = self.callback(*data)
            self.clear()
            if isinstance(result, str):
                self.callback2("Error", result)
            else:
                if self.callback1:
                    self.callback1()

    def return_data(self):
        new_username = self.ent_username.get()
        new_pass = self.ent_pass.get()
        new_data = (new_username, new_pass)
        return [data if not data.isspace() and data != "" else None for data in new_data]

    def clear(self):
        self.ent_username.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)


if __name__ == "__main__":
    win = tk.Tk()
    fr = Edit1("Tabasom",win)
    win.mainloop()