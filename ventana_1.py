# se importala libreria tkinter 
from tkinter import *
# -----------------------------
# funciones de la app 
# -----------------------------


# -----------------------------
# ve ntana principal de la app
# -----------------------------

# se declara una variable  llamada ventana_principal, que anquiere las caracteristicas de un juego

ventana_principal= Tk()

# Titulo de ventana 
ventana_principal.title("David macias ")

# Tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilita boton de minimizar la ventana 
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg= "gray")

# -----------------------------
# frame 1 
# -----------------------------

frame_1  = Frame(ventana_principal)
frame_1.config(bg = "yellow", width=700,height=240)
frame_1.place(x=50, y=10)

frame_2  = Frame(ventana_principal)
frame_2.config(bg = "blue", width=700,height=240)
frame_2.place(x=50, y=250)

frame_3  = Frame(ventana_principal)
frame_3.config(bg = "red", width=700,height=240)
frame_3.place(x=50, y=370)


# metodo principal que despliega la ventana en pantalla 
ventana_principal.mainloop()