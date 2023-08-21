from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import windows_app.hora_dia as dia
import windows_app.horario_tarde as tarde
import windows_app.horario_noche as noche
import windows_app.hora_dia as dia
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END


def horarioBien(root, mainFrame):
    root.title("Horarios de líneas de tren")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo, vaerDropBox


    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO_BIENVENIDA.png"))

    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    


    Button(mainFrame, text = "Continuar", width = 10,relief="flat",font=("Inter", 12,"bold"),bg="#FFFFFF",fg="#000000", command = lambda: dia.horaMAÑANA(root, mainFrame)).place(x = 134, y = 600)


