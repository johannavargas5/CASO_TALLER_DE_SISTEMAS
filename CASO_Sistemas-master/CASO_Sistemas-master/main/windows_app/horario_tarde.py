from tkinter import *
from tkinter import ttk
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import windows_app.horario_noche as noche
import windows_app.hora_dia as dia
import helpers.readfiles as readfiles
import windows_app.horario_tarde as tarde
import windows_app.HOME as ho
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

def horaTARDE(root, mainFrame):
    root.title("Horarios de líneas de tren")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo, vaerDropBox
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO2.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    categoriesNUMEROSvar = ['Dia', 'Tarde', 'Noche']
    Label(mainFrame, text = "SELECCIÓN DE FASES DEL DÍA : ", relief= "flat", bg="#EFFBFB", font=("Inter", 10)).place(x = 12, y = 90)
    vaerDropBox= ttk.Combobox(mainFrame,font=("Inter", 11,"bold"),width = 10)
    vaerDropBox.set("Fases del Día")

    vaerDropBox.set("Tarde")
    vaerDropBox["values"]  = categoriesNUMEROSvar
    vaerDropBox.place(x = 250, y = 90)
    
    
    Button(mainFrame, text = "Continuar", width = 25,relief="flat",font=("Inter", 12,"bold"),bg="#000000",fg="#ffffff", command = lambda: Selec_Rooty()).place(x = 60, y = 290)

    Button(mainFrame, text = "Continuar", width = 25,relief="flat",font=("Inter", 12,"bold"),bg="#000000",fg="#ffffff", command = lambda: Selec_Rooty(root, mainFrame)).place(x = 60, y = 290)
    
    Button(mainFrame, text = "Home", width = 7, bg="#03989e", relief="flat",font=("Inter", 13,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 253, y = 613)

#RUTAS
def Selec_Rooty(root, mainFrame):
    a = vaerDropBox.get()
    
    if a == 'Dia':
        dia.horaMAÑANA(root, mainFrame)
    elif a == 'Tarde':
        tarde.horaTARDE(root, mainFrame)
    else:
        noche.horaNOCHE(root, mainFrame)
