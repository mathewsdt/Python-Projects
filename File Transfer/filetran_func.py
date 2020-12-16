from tkinter import *
import tkinter as tk
import shutil
import os
import time
from tkinter import filedialog
from tkinter import messagebox


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
    if filePath:
        entry.insert(0,filePath+"/")



def ask_quit(self):
    if messagebox.askokcancel("Close program", "Okay to close?"):
       self.master.destroy()
       os._exit(0)


def check(self):
    src = self.src_disp.get()
    des = self.des_disp.get()

    lsdir = os.listdir(src)
    validFiles = []
    period = time.time()-86400

    for i in lsdir:
        mtime = os.path.getmtime(src+i)
        if mtime >= period:
            validFiles.append(i)
    if validFiles:
       for i in validFiles:
           shutil.move(src+i,des)
       messagebox.showinfo("Files transfered","Transfer was a success!")

   


if __name__ == "__main__":
    pass
