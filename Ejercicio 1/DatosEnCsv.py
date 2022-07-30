from GUI import GUI
from tkinter import messagebox

try:

    GUI()

except:

    titulo="ERROR"
    mensaje="No se pudo ejecutar"
    messagebox.showerror(titulo,mensaje)