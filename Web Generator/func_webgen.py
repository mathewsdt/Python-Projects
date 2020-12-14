import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import webbrowser

import main_webgen
import gui_webgen

def ask_quit(self):
    if messagebox.askokcancel("Are you sure you want to exit program? "):
        self.master.destroy()
        os._exit(0)

def addToBody(self):
    #try:
    body = self.txt_body.get("1.0",END)
    f = open("index.html","w")
    texttoadd = "<html> \n<body> \n {} \n </body>\n <html>".format(body)
    f.write(texttoadd)
    messagebox.showinfo("Nice work!", "File suscessfully created")
    f.close()
    webbrowser.open("index.html")
    #except:
        #messagebox.showinfo("Sorry, problem occured", "Please try again")



if __name__ == "__main__":
    pass
