from tkinter import *
import windows_app.BIENV as bienv
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def REC(root, mainFrame):
    root.title("REGISTRO")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTRARSE.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################
    
    nom = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = nom, font=("Inter", 22), relief="flat").place(x = 60, y = 182)
    ape = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = ape, font=("Inter", 22), relief="flat").place(x = 60, y = 260)
    cor = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = cor, font=("Inter", 22), relief="flat").place(x = 95, y = 340)
    passw = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = passw, font=("Inter", 22), relief="flat").place(x = 95, y = 410)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Registrarse", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: bienv.BIENVN(root, mainFrame)).place(x = 100, y = 490)

