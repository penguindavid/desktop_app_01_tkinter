from tkinter import *

# --------------------------------- 
# Ventana principal de la app
# --------------------------------- 

ventana_principal = Tk()
ventana_principal.title("Bandera de Francia")
ventana_principal.geometry("600x300")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="gray")

# --------------------------
# Frame 1
# --------------------------

frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=200, height=280)
frame_azul.place(x=10, y=10)

# --------------------------
# Frame 2
# --------------------------

frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white", width=200, height=280)
frame_blanco.place(x=200, y=10)

# --------------------------
# Frame 3
# --------------------------

frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=200, height=280)
frame_rojo.place(x=390, y=10)

# ---------------------------------
# Mostrar la ventana
# ---------------------------------

ventana_principal.mainloop()

