import tkinter as tk
ventana = tk.Tk()

ventana.geometry("500x500+150+150")
ventana.title("La app de Fran Collao")
tk.Label(ventana,text="Hola, esta es mi primera interfaz")
ventana.mainloop() #similar a bucle infinito para que no se cierre.