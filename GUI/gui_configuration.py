import tkinter as tk

default_bg = {"frame": "#00a693",
              "button": "white",
              "tk": "green", 
              "toplevel": "yellow",
              "label": "#00a693"}

class Tk(tk.Tk):
    
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg = default_bg["tk"])
        self.bind("<Configure>", self.auto_geometry)
        
    def auto_geometry(self, event):
        '''
        screen sizes are actually your resolution. e.g. mine is 1600*900.
        tk sizes are size of panel created by this class(ManagerView).
        more widgets within this class, more tk size.
        '''
        
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        tk_w= self.winfo_width()
        tk_h = self.winfo_height()
        place_x = int(screen_w / 2) - int(tk_w /2)
        place_y = int(screen_h / 2) - int(tk_h / 2)
        if tk_w != 1 and tk_h != 1:
            self.geometry(f"{tk_w}x{tk_h}+{place_x}+{place_y}")
            self.unbind("<Configure>")  # need it here, trust me.  

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
        
class Label(tk.Label): 
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = default_bg["label"]
        super().__init__(master, **kwargs)

class Button(tk.Button):
    def __init__(self, master = None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = default_bg["button"]
        if "relief" not in kwargs:
            kwargs["relief"] = tk.GROOVE
        if "width" not in kwargs:
            kwargs["width"] = 10
        if "cursor" not in kwargs:
            kwargs["cursor"] = "hand2"
        if "activebackground" not in kwargs:
            kwargs["activebackground"] = "#B8D3FF"
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
            