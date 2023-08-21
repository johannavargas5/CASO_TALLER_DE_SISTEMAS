from tkinter import *
import helpers.readfiles as readfiles
import windows_app.BIENV as bienv
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END


#* Estructura de la ventana del Dashboard general.
def INICIAR(root, mainFrame):
    root.title("Iniciar sesión")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\LOG_INICIAL.png"))
    
    
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################    
    nom = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = nom,font=("Inter", 25),relief="flat").place(x = 150, y = 100)
    ap = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = ap,font=("Inter", 25)).place(x = 150, y = 200)
    cor = StringVar()
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: bienv.BIENVN(root, mainFrame)).place(x = 200, y = 600)