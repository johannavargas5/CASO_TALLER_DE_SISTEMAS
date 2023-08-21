from tkinter import *
import windows_app.RECARGA as reca
import windows_app.HOME as home
import windows_app.ENVIONO as envia
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def rREserva_vista(root, mainFrame):
    root.title("RESERVA")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\RESERVA4.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    Button(mainFrame, text = "Home", width = 7, bg="#03989e", relief="flat",font=("Inter", 13,"bold"), command = lambda: home.HOM(root, mainFrame)).place(x = 253, y = 613)
    