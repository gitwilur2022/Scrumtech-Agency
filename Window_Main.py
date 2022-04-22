from cgitb import text
from distutils.cmd import Command
from msilib.schema import RadioButton
from multiprocessing.sharedctypes import Value
import tkinter as tk
from ast import Pass
import re
from tkinter.constants import *
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
import time
import hashlib
from tkinter import StringVar, Variable, ttk
import openpyxl._constants as constants
import openpyxl
from openpyxl import workbook
from openpyxl import load_workbook
from SearchUsers import SearchUsersWilur
from CreateUsersWilur import CreateUsers


class WindowMainMyFirstAplication():

    def __init__(MyFirstAplication):
        MyFirstAplication= tk.Tk()
        MyFirstAplication.attributes('-fullscreen', True)  
        MyFirstAplication.bind("<F11>",
                         lambda event: MyFirstAplication.attributes("-fullscreen",
                                    not MyFirstAplication.attributes("-fullscreen")))
        MyFirstAplication.bind("<Escape>",
                         lambda event: MyFirstAplication.attributes("-fullscreen",
                                    False))
        MyFirstAplication.title("SUPERWILUR")
        MyFirstAplication.configure(bg='linen')
        MyFirstAplication.iconbitmap("wilur.ico")
        MyFirstAplication.resizable(0,0)
        MyFirstAplication.foto=tk.PhotoImage(file="ilogo.png")
        label6=tk.Label(image=MyFirstAplication.foto).place(x=0,y=0)

        ButtonEnterRegisterUserSW=tk.Button(MyFirstAplication,text="CREA TU LOGIN",
        bg="pale turquoise",fg="red",
        font=("Elephan",12),borderwidth=5,).place(x=205,y=138)

        ButtonEnterRegisterUserSW=tk.Button(MyFirstAplication,text="ENTRAR COMO USUSARIO",
        command=SearchUsersWilur,bg="pale turquoise",fg="red", 
        font=("Elephan",12),borderwidth=5,).place(x=357,y=138)

        ButtonEnterRegisterUserSW=tk.Button(MyFirstAplication,text="ENTRAR COMO ADMINISTRADOR",
        bg="pale turquoise",fg="red", 
        font=("Elephan",12),borderwidth=5,).place(x=1080,y=138)
        

        ButtonEnterRegisterUserSW=tk.Button(MyFirstAplication,text="Salir de la aplicación",
        command=MyFirstAplication.quit,bg="pale turquoise",fg="red", 
        font=("Elephan",12),borderwidth=5,).place(x=1365,y=138)
        MyFirstAplication.mainloop()
if __name__ == '__main__':
    app = WindowMainMyFirstAplication()