import tkinter as tk        #importo libreria para crear interfaces
import ttkbootstrap as ttk



ventana = ttk.Window(themename="darkly")           #creo una nueva ventana y le doy un estilo oscuro a la interfaz



ventana.geometry("500x500+150+150")         #le doy dimensiones a mi ventana
ventana.title("La Calculadora de Fran Collao")          #le añado un titulo a mi ventana

operando1 = tk.IntVar()             #creo variable de tkinter para guardar info
operando2 = tk.IntVar()             #creo variable de tkinter para guardar info

def calcula():              #funcion que se va ejecutar al pulsar el boton
    global etiquetaresultado        #meto aqui dentro la variable etiquetaresultado
    print("voy a calular algo")     #mensaje con lo que voy hacer
    op1 = operando1.get()           #obtengo el valor del campo 1 y lo almaceno en la variable op1
    op2 = operando2.get()           #obtengo el valor del campo 1 y lo almaceno en la variable op2
    calculo = op1 + op2             #realizo calculo
    etiquetaresultado.config(text=str(calculo))     #imprimo ese calculo en la pantalla, haciendo conversion ya que la salida el tipo text


tk.Label(               #creo etiqute inicial
    ventana,
    text="Introduce el operando 1: "
).pack(padx=10,pady=10)

tk.Entry(                       #creo campo de texto
    ventana,
    textvariable=operando1,
    width=600
).pack(padx=10,pady=10)

tk.Label(                    #creo etiquta para operador 2
    ventana,
    text="Introduce el operando 2: "
).pack(padx=10,pady=10)

tk.Entry(                    #creo campo de texto para el 2
    ventana,
    textvariable=operando2,
     width=600
).pack(padx=10,pady=10)




tk.Label(               #creo etiqueta para el boton
    ventana,        
    text="pulsa para obtener resutado "
).pack(padx=10,pady=10)

tk.Button(          #creo el boton
    ventana,
    text="CALCULA",
     width=600,
    command=calcula
).pack(padx=10,pady=10)


tk.Label(           #creo etiqueta pra poner el resultado
    ventana,
    text="El resultado es:  "
).pack(padx=10,pady=10)

etiquetaresultado = tk.Label(       #creo etiqueta pero en memoria para luego llamarla
    ventana,
    text="0"
)

etiquetaresultado.pack(padx=10,pady=10)     #empaqueto la etiqueta





ventana.mainloop()

