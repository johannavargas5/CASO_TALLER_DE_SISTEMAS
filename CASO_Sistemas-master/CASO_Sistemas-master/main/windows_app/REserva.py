from tkinter import *
import windows_app.HOME as home
import windows_app.Reserva_un as unRES
import windows_app.Resrva_dos as doRES
import windows_app.Reserva_tre as treRES
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def RESERVA(root, mainFrame):
    root.title("RESERVA")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\is_RESERVA1.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)

    Button(mainFrame, text = "MIRAR", width = 15,relief="flat",bg = "#03989e", font=("Inter", 15,"bold"), command = lambda: unRES.RESer_un(root, mainFrame)).place(x = 95, y = 110)
    Button(mainFrame, text = "RESERVAR", width = 15,relief="flat",bg = "#03989e", font=("Inter", 15,"bold"), command = lambda: doRES.RESer_do(root, mainFrame)).place(x = 95, y = 230)
    Button(mainFrame, text = "QR", width = 15,relief="flat",bg = "#03989e", font=("Inter", 15,"bold"), command = lambda: treRES.RESer_tre(root, mainFrame)).place(x = 95, y = 350)
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Home", width = 7, bg="#03989e", relief="flat",font=("Inter", 13,"bold"), command = lambda: home.HOM(root, mainFrame)).place(x = 253, y = 613)
