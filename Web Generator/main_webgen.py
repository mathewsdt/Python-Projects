#Python Ver:    3.7.8
#
#Author:        Dominique Mathews
#
#Purpose:       GUI to enable users to set body text for new web page
from tkinter import *
import tkinter as tk
import tkinter.messagebox


#imported modules to have access to
import gui_webgen
import func_webgen

# Frame is the Tkinter frame class that class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(500,500)# (Height, Width)
        self.master.maxsize(500,500)
        self.master.title("Web Page Generator")

        self.master.protocol("WM_DELETE_WINDOW", lambda: func_webgen.ask_quit(self))


        # loads GUI widgets from gui_webgen module
        gui_webgen.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
