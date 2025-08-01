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
frame_1.config(bg = "red", width=730,height=240)
frame_1.place(x=50, y=10)

# -----------------------------
# frame 2
# -----------------------------

frame_2  = Frame(ventana_principal)
frame_2.config(bg = "red", width=730,height=240)
frame_2.place(x=50, y=250)

# -----------------------------
# frame 3
# -----------------------------

frame_3  = Frame(ventana_principal)
frame_3.config(bg = "white", width=730,height=90)
frame_3.place(x=50, y=170)

# -----------------------------
# frame 4
# -----------------------------

frame_4  = Frame(ventana_principal)
frame_4.config(bg = "white", width=90,height=480)
frame_4.place(x=170, y=10)
# -----------------------------
# frame 5
# -----------------------------

frame_5  = Frame(ventana_principal)
frame_5.config(bg = "dark blue", width=730,height=70)
frame_5.place(x=50, y=180)

# -----------------------------
# frame 6
# -----------------------------

frame_6  = Frame(ventana_principal)
frame_6.config(bg = "darkblue", width=80,height=480)
frame_6.place(x=170, y=10)


# metodo principal que despliega la ventana en pantalla 
ventana_principal.mainloop()

