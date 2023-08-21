from tkinter import *
import helpers.readfiles as readfiles
import windows_app.BIENV as bienv
import windows_app.HOME as ho
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

    

#* Estructura de la ventana del Dashboard general.
def BIENVN(root, mainFrame):
    root.title("Bienvenido")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\BIENVENIDA_APP.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)

##############################    
    Button(mainFrame, text = "Siguiente", width = 10,relief="flat",bg = "#FFFFFF",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 128, y = 560)


#*falta ruta home (lambda)