from tkinter import *
import windows_app.inic as ini
import helpers.readfiles as readfiles

#* Estructura general
root = Tk()
root.resizable(0,0)
mainFrame = Frame(root)
ini.Login(root, mainFrame)
my_path = readfiles.Route()
root.iconbitmap(my_path + "\main\images\APP.ico")


def quit_me():
    root.quit()
    root.destroy() 
    

root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()