import tkinter as tk
ventana = tk.Tk()

ventana.geometry("500x500+150+150")
ventana.title("La app de Fran Collao")

def queEjecuto():
    print("has sido valiente")
    global texto
    texto.config(text="Este texto ha salido desde una funcion")

texto = tk.Label(
    ventana,
    text="Hola esta es mi app :)"



)

#tk.Label(ventana,text="Hola, esta es mi primera interfaz").pack(padx=20,pady=20)

texto.pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)
tk.Button(ventana,text="se valiente y pinchame",command=queEjecuto).pack(padx=10,pady=10)





ventana.mainloop() #similar a bucle infinito para que no se cierre.

