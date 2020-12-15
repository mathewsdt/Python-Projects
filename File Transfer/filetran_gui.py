from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import filetran_main
import filetran_func

def load_gui(self):
    # buttons
    self.btn_brws1 = tk.Button(self.master,width=15,height=1,text="Source...",command=lambda: filetran_func.browse(self,"src"))
    self.btn_brws1.grid(row=0,column=0,padx=(20,30),pady=(40,0),sticky=W)

    self.btn_brws2 = tk.Button(self.master,width=15,height=1,text="Destination...",command=lambda: filetran_func.browse(self,"des"))
    self.btn_brws2.grid(row=1,column=0,padx=(20,30),pady=(10,0),sticky=W)

    self.btn_cl = tk.Button(self.master,width=15,height=2,text="Close Program",command=lambda: filetran_func.ask_quit(self))
    self.btn_cl.grid(row=2,column=2,padx=(0,20),pady=(10,10),sticky=E)

    # Source & Destination Paths
    self.src_disp = tk.Entry(self.master, width=50, font=('Helvetica', 10))
    self.src_disp.grid(row=0, column=1, columnspan=2, padx=(0, 20), pady=(40, 0), sticky=N+W)

    self.des_disp = tk.Entry(self.master, width=50, font=('Helvetica', 10))
    self.des_disp.grid(row=1, column=1, columnspan=2,  padx=(0, 20), pady=(10, 0), sticky=N+W)


if __name__ == "__main__":
    pass
