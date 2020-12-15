from tkinter import *
import tkinter as tk

import filetran_gui
import filetran_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("File Find & Transfer")
       
        self.master.protocol("WM_DELETE_WINDOW", lambda: filetran_func.ask_quit(self))


        #load the gui
        filetran_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
