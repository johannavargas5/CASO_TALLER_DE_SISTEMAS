from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

#* Estructura de la ventana del Dashboard general.
def horario(root, mainFrame):
    root.title("Horarios de líneas de tren")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()

    global logo, vaerDropBox
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    #* Función para cerrar y destruir la ventana al cerrar la aplicación externamente.
