from tkinter import *
import windows_app.METODO_PAGO as met_pago
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def BIEN_REC(root, mainFrame):
    root.title("Bienvenida a la Sección de Recargas")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\Bien_recargas.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################

    Button(mainFrame, text = "Continuar", width = 10, bg="#FFFFFF", relief="flat",font=("Inter", 15,"bold"), command = lambda: met_pago.MET_PAGO(root, mainFrame)).place(x = 125, y = 575)
