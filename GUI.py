# this module should define an api for main.py. classes and their methods
# must be able to do any need of the gui. in this project any toplevel class
# must be named like: 'CustomerTop" also any frame class must be named like:
# 'CustomerTransferView' or 'CustomerCreateAccountView' 'Top' classes must
# be defined in this module and 'View' classes must be defined in.. other
# gui modules like: gui_customer.py or gui_manager.py and etc.
import tkinter as tk

Toplevel = tk.Toplevel  # you can create a Toplevel class to create themes :)


class CustomerTop(Toplevel):
    # any thing that the backend want to do must be possible by the methods.
    # two examples:
    def show_error(self, message: str):
        pass

    def show_success(self, message: str = "successful"):
        pass


class ManagerTop(Toplevel):
    pass
