from tkinter import *
import helpers.readfiles as readfiles
import windows_app.BIENV as bienv
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.
def NUEVO_INIC_REC(root, mainFrame):
    root.title("Nuevo Inicio de Sesión")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\INGRESAR.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################    
    email = StringVar()
    Entry(mainFrame, width = 12, borderwidth = 2, textvariable = email,font=("Inter", 25),relief="flat").place(x = 100, y = 240)
    contra = StringVar()
    Entry(mainFrame, width = 12, borderwidth = 2, textvariable = contra,font=("Inter", 25),relief="flat").place(x = 100, y = 318)
    
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Ingresar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: bienv.BIENVN(root, mainFrame)).place(x = 100, y = 440)