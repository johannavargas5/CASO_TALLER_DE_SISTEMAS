from tkinter import *
import windows_app.EXI_RECARGA as exi_rec
import windows_app.METODO_PAGO as met_pago
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    
#* Estructura de la ventana del Dashboard general.

def RECARGA_TRAIN(root, mainFrame):
    root.title("RECARGAS")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\DATOS_RECARGA.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################
    
    num_tarjeta = StringVar()
    Entry(mainFrame, width = 12, borderwidth = 2, textvariable = num_tarjeta, font=("Inter", 22), relief="flat").place(x = 110, y = 175)
    mon = StringVar()
    Entry(mainFrame, width = 6, borderwidth = 2, textvariable = mon, font=("Inter", 22), relief="flat").place(x = 150, y = 262)
    tarj_pago = StringVar()
    Entry(mainFrame, width = 12, borderwidth = 2, textvariable = tarj_pago, font=("Inter", 22), relief="flat").place(x = 110, y = 355)
    fv = StringVar()
    Entry(mainFrame, width = 4, borderwidth = 2, textvariable = fv, font=("Inter", 22), relief="flat").place(x = 107, y = 440)
    cvv = StringVar()
    Entry(mainFrame, width = 4, borderwidth = 2, textvariable = cvv, font=("Inter", 22), relief="flat").place(x = 235, y = 440)
    ema = StringVar()
    Entry(mainFrame, width = 12, borderwidth = 2, textvariable = ema, font=("Inter", 22), relief="flat").place(x = 102, y = 522)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Pagar", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: exi_rec.EXITO_RECARGA(root, mainFrame)).place(x = 127, y = 595)
    Button(mainFrame, text = "Regresar", width = 8, bg="#FFFEFD", relief="flat",font=("Inter", 13,"bold"), command = lambda: met_pago.MET_PAGO(root, mainFrame)).place(x = 10, y = 15)
