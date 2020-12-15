from tkinter import *
import tkinter as tk
import shutil
import os
import time


import filetran_main
import filetran_gui


def browse(self,btn):
    if btn == "src":
        entry = self.src_disp
    if btn == "des":
        entry = self.des_disp
    entry.config(state='normal')
    entry.delete(0,"end")
    filePath = filedialog.askdirectory()



def ask_quit(self):
    if messagebox.askokcancel("Close program", "Okay to close?"):
       self.master.destroy()
       os._exit(0)

   


if __name__ == "__main__":
    pass
