from tkinter import *
import windows_app.REG as rec
import windows_app.LOG as log
import helpers.readfiles as readfiles
from PIL import Image, ImageTk

#* Estructura de la ventana de Inicio.
def Login(root, mainFrame):
    root.title("LOGIN")
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\INICIAL.png"))
    
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    Button(mainFrame, text = "REGISTRO", bg="#a0d3d8", width = 10, height = 3, relief="flat",fg="#000000",font=("Inter", 15,"bold"), command = lambda: rec.REC(root, mainFrame)).place(x = 125, y = 360)

    Button(mainFrame, text = "INICIAR SESIÓN", bg="#a0d3d8", width = 13, height = 3, relief="flat",fg="#000000",font=("Inter", 15,"bold"), command = lambda: log.LOG(root, mainFrame)).place(x = 110, y = 510)
    
