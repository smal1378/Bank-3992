import tkinter as tk
Default_Theme = "white"
class Tk(tk.Tk):
    def __init__(self):
        super(Tk, self).__init__()
        self.config(bg=Default_Theme)
class Toplevel(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        super(Toplevel, self).__init__(master, **kwargs)
class Entry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        if "relief" not in kwargs:
            kwargs["relief"] = "solid"
        if "bd" not in kwargs:
            kwargs["bd"] = 1
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        super(Entry, self).__init__(master, **kwargs)
class Frame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        super(Frame, self).__init__(master, **kwargs)
class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        if "relief" not in kwargs:
            kwargs["relief"] = "solid"
        if "bd" not in kwargs:
            kwargs["bd"] = 1
        if "cursor" not in kwargs:
            kwargs["cursor"] = "hand2"
        super(Button, self).__init__(master, **kwargs)
class Label(tk.Label):
    def __init__(self, master=None, **kwargs):
        if "bg" not in kwargs:
            kwargs["bg"] = Default_Theme
        if "cursor" not in kwargs:
            kwargs["cursor"] = "heart"
        super(Label, self).__init__(master, kwargs)

class View_karmand(Toplevel):
      def __init__(self):
         super(View_karmand, self).__init__()
         #self.user=user
         #self.title(f"logged in as {user.username}")
         
      def View_karmand(self):
          self.b1= Button(self,text="daryaftvajh", command=self.daryaftvajh).grid(row=1,column=2,pady=20)
      def daryaftvajh():
          pass
        
       
        
      def show_error():
          pass

root = View_karmand()
root.View_karmand()
root.geometry("400x100")
tk.mainloop()



      
         
         
      
         
                
         
     
     

      










    
       
         
         
      
         
                
         
     
     

      
















































		
       
         
         
      
         
                
         
     
     

      




























