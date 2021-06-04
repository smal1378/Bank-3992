import tkinter as tk
from ..gui_configuration import Button, Frame, Label


class Mojoodi1(Frame):

    def __init__(self, master=None, callback=None,callback1=None,callback2=None):
        super().__init__(master)
        self.callback = callback
        self.callback1 = callback1
        self.callback2 = callback2
        self.pack(expand=True)

        self.lbl_mm = Label(self, text="موجودی حساب:",bg="#e4e8d5")
        self.lbl_mm.grid(row=0, column=0,padx=10, pady=10, sticky="w")

        self.lbl_mm1 = Label(self, text=f" {self.callback}ریال ", bg="#e4e8d5")
        self.lbl_mm1.grid(row=0, column=1,padx=10, pady=10, sticky="w")

        self.btn_submit = Button(self, text="تایید",command=self.Close)
        self.btn_submit.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

    def Close(self):
        Frame.destroy(self)

    def data(self):
        mojoodi = self.callback()
        new_data = (mojoodi)
        if all(item.isalnum() for item in new_data):
            return new_data

if __name__ == "__main__":
    win = tk.Tk()
    fr = Mojoodi1(win)
    win.mainloop()
