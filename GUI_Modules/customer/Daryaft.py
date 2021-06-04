import tkinter as tk
from ..gui_configuration import Button, Frame, Label


class Daryaft1(Frame):
    def __init__(self, master=None, callback=None, callback1=None, callback2=None,callback3=None):
        super().__init__(master)
        self.callback = callback
        self.callback1 = callback1
        self.callback2 = callback2
        self.callback3 = callback3
        self.pack(expand=True)

        self.lbl_mv = Label(self, text="میزان وجه مورد نظر:",bg="#e4e8d5")
        self.lbl_mv.grid(row=0, column=0,padx=10, pady=10, sticky="w")

        self.ent_mv = tk.Entry(self)
        self.ent_mv.grid(row=0, column=1)

        self.btn_submit = Button(self, text="دریافت",command=self.submit)
        self.btn_submit.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

        self.ent_mv.focus_set()

        self.entries = [ent for ent in self.winfo_children() if isinstance(ent, tk.Entry)]
        self.ent_mv.bind("<Return>", lambda _: self.entries[1].focus_set())


    def submit(self):
        data = self.return_data()
        x=int(self.callback)-int(data)
        self.callback=x

    def return_data(self):
        new_mv = self.ent_mv.get()
        new_data = (new_mv)
        if all(item.isalnum() for item in new_data):
            return new_data

    def clear(self):
        self.ent_mv.delete(0, tk.END)


if __name__ == "__main__":
    win = tk.Tk()
    fr = Daryaft1(win)
    win.mainloop()
