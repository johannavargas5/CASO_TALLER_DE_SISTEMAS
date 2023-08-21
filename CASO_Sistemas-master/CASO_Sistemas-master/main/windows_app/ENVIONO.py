from tkinter import *
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import windows_app.HOME as home
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def Enviar_NOti(root, mainFrame):
    root.title("NOTIFICACIONES")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\lNOTIFICACIONES2.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    notifi=StringVar
    Entry(mainFrame, width = 12, borderwidth = 8,bg = "#ebfafe", textvariable = notifi,font=("Inter"),relief="flat").place(x = 90, y = 180)
    
################################
    Button(mainFrame, text = "Home", width = 7, bg="#03989e", relief="flat",font=("Inter", 13,"bold"), command = lambda: home.HOM(root, mainFrame)).place(x = 253, y = 613)
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "ENVIAR", width = 10, bg = "#03989e", relief="flat",font=("Inter", 15,"bold"), command = lambda: notifi).place(x = 125, y = 450)
