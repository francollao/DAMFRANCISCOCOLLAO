'''
Programa de base IVA e IRPF


FRAN COLLAO

'''


import tkinter as tk        #importamos tk inter como tk

ventana = tk.Tk() #creamos la ventana 
ventana.geometry("600x600+200+200")         #le damos las dimensiones y el bordeado de las esquinas 
ventana.title("EXAMEN DE PROGRAMACION")         #ponemos titulo a la ventana

baseimpo = tk.IntVar() #almacenamos la variable en formato de numero ya que el tipo de dato es un numero



tk.Label(ventana,
         text="Introduce una base imponible").pack(padx=15,pady=15)


tk.Entry(
    textvariable=baseimpo

).pack(padx=15,pady=15)


##creamos el boton a continuacion 

#creamos etiqueta

tk.Label(ventana,
         text="pulsame para saber datos").pack(padx=15,pady=15)

#creamos boton

tk.Button(ventana,
          text="SABRAS LOS DATOS"
        #  command=
).pack(padx=15,pady=15)














ventana.mainloop()      #con esto hacemos que la ventana salga por pantalla y sea visible 

