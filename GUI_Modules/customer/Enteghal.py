import tkinter as tk
from ..gui_configuration import Button, Frame, Label


class Enteghal1(Frame):


    def __init__(self, master=None, callback=None,callback1=None,callback2=None):
        super().__init__(master)
        self.callback = callback
        self.callback1 = callback1
        self.callback2 = callback2
        self.pack(expand=True)

        self.lbl_ev = Label(self, text="میزان وجه مورد نظر:",bg="#e4e8d5")
        self.lbl_ev.grid(row=0, column=0,padx=10, pady=10, sticky="w")
        self.lbl_ev1 = Label(self, text="شماره حساب 12 رقمی:",bg="#e4e8d5")
        self.lbl_ev1.grid(row=1, column=0,padx=10, pady=10, sticky="w")

        self.ent_ev = tk.Entry(self)
        self.ent_ev.grid(row=0, column=1)
        self.ent_ev1 = tk.Entry(self)
        self.ent_ev1.grid(row=1, column=1)

        self.btn_submit = Button(self, text="انتقال",command=self.submit)
        self.btn_submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.ent_ev.focus_set()
        self.ent_ev1.focus_set()

        self.entries = [ent for ent in self.winfo_children() if isinstance(ent, tk.Entry)]
        self.ent_ev.bind("<Return>", lambda _: self.entries[1].focus_set())
        self.ent_ev1.bind("<Return>", lambda _: self.entries[2].focus_set())

    def submit(self):
        data = self.return_data()
        if self.callback:
            result = self.callback(*data)
            self.clear()
            if isinstance(result, int):
                if self.callback2:
                    self.callback2("Error", result)
            else:
                if self.callback1:
                    self.callback1()

    def return_data(self):
        new_ev = self.ent_ev.get()
        try:
            new_ev=int(new_ev)
        except:
            pass
        if isinstance(new_ev, int):
            pass
        else:
            self.lbl_er = Label(self, text="مبلغ غیر مجاز", bg="#ed0909")
            self.lbl_er.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        new_ev1 = self.ent_ev1.get()
        try:
            new_ev1=int(new_ev1)
        except:
            pass
        if isinstance(new_ev1, int):
            if len(str(new_ev1))==12:
                pass
            else:
                self.lbl_er1 = Label(self, text="شماره حساب غیر مجاز", bg="#ed0909")
                self.lbl_er1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        else:
            self.lbl_er1 = Label(self, text="شماره حساب غیر مجاز", bg="#ed0909")
            self.lbl_er1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


        new_data = (new_ev,new_ev1)
        print(str(new_data))
        if all(item.isalnum() for item in new_data):
            return new_data

    def clear(self):
        self.ent_ev.delete(0, tk.END)
        self.ent_ev1.delete(0, tk.END)


if __name__ == "__main__":
    win = tk.Tk()
    fr = Enteghal1(win)
    win.mainloop()
