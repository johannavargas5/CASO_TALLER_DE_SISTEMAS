from tkinter import *
import helpers.readfiles as readfiles
import windows_app.BIENV as bienv
import windows_app.REC_CONT as recp_con
import windows_app.NUEVO_INICIO_REC as nuevo_rec
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.
def RECUPERA(root, mainFrame):
    root.title("Recuperación de Contraseña")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\RECUPERACIÓN_CONTRA.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)

###############################
    
    corre = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = corre, font=("Inter", 22), relief="flat").place(x = 95, y = 265)
    nue = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = nue, font=("Inter", 22), relief="flat").place(x = 95, y = 340)
    nuev2 = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = nuev2, font=("Inter", 22), relief="flat").place(x = 95, y = 415)
    
##############################    
    Button(mainFrame, text = "Continuar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: nuevo_rec.NUEVO_INIC_REC(root, mainFrame)).place(x = 105, y = 515)
