from tkinter import *
import windows_app.HOME as ho
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def EXITO_RECARGA(root, mainFrame):
    root.title("Recarga Exitosa")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\EXITO_RECARGA.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################

    Button(mainFrame, text = "Regresar a Home", width = 13, bg="#FFFFFF", relief="flat",font=("Inter", 13,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 118, y = 595)
