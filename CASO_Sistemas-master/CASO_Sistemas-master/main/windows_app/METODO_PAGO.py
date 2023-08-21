from tkinter import *
import windows_app.RECARGA as recar_train
import windows_app.HOME as ho
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def MET_PAGO(root, mainFrame):
    root.title("SELECCIÓN DE MÉTODO DE PAGO")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\METODO_DE_PAGO.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################
    
    visa = StringVar()
    Checkbutton(mainFrame, textvariable = visa, bg="#FFFFFF",font=("Inter", 22), relief="flat").place(x = 45, y = 260)
    mastercard = StringVar()
    Checkbutton(mainFrame, textvariable = mastercard, bg="#FFFFFF",font=("Inter", 22), relief="flat").place(x = 198, y = 260)
    dinners = StringVar()
    Checkbutton(mainFrame, textvariable = dinners, bg="#FFFFFF",font=("Inter", 22), relief="flat").place(x = 45, y = 360)
    american = StringVar()
    Checkbutton(mainFrame, textvariable = american, bg="#FFFFFF",font=("Inter", 22), relief="flat").place(x = 198, y = 360)
    condi = StringVar()
    Checkbutton(mainFrame, textvariable = condi, bg="#FFFFFF",font=("Inter", 22), relief="flat").place(x = 52, y = 455)
    
################################
    
    Button(mainFrame, text = "Siguiente", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: recar_train.RECARGA_TRAIN(root, mainFrame)).place(x = 125, y = 540)
    Button(mainFrame, text = "Regresar", width = 8, bg="#FFFEFD", relief="flat",font=("Inter", 13,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 10, y = 15)
