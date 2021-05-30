import tkinter as tk

default_bg = {"frame": "gray",
              "button": "white",
              "tk": "green", 
              "toplevel": "yellow"}

class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg = default_bg["tk"])

class Toplevel(tk.Toplevel):
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = default_bg["toplevel"]
        super().__init__(master, **kwargs)

class Frame(tk.Frame):
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = default_bg["frame"]
        super().__init__(master, **kwargs)

class Button(tk.Button):
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = default_bg["button"]
        if "relief" not in kwargs:
            kwargs["relief"] = tk.GROOVE
        if "width" not in kwargs:
            kwargs["width"] = 10
        super().__init__(master, **kwargs)
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)
    def onEnter(self, event):
        self.config(bg = "#D8F3FF")
    def onLeave(self, event):
        if hasattr(self, "default_bg"):
            self.config(bg = self["bg"])
        else:
            self.config(bg = default_bg["button"])
            