import tkinter as tk
ventana = tk.Tk()

ventana.geometry("500x500+150+150")
ventana.title("La Calculadora de Fran Collao")

operando1 = tk.IntVar()
operando2 = tk.IntVar()

def calcula():
    global etiquetaresultado
    print("voy a calular algo")
    op1 = operando1.get()
    op2 = operando2.get()
    calculo = op1 + op2
    etiquetaresultado.config(text=str(calculo))


tk.Label(
    ventana,
    text="Introduce el operando 1: "
).pack(padx=10,pady=10)

tk.Entry(
    ventana,
    textvariable=operando1
).pack(padx=10,pady=10)

tk.Label(
    ventana,
    text="Introduce el operando 2: "
).pack(padx=10,pady=10)

tk.Entry(
    ventana,
    textvariable=operando2
).pack(padx=10,pady=10)




tk.Label(
    ventana,
    text="pulsa para obtener resutado "
).pack(padx=10,pady=10)

tk.Button(
    ventana,
    text="CALCULA",
    command=calcula
).pack(padx=10,pady=10)


tk.Label(
    ventana,
    text="El resultado es:  "
).pack(padx=10,pady=10)

etiquetaresultado = tk.Label(
    ventana,
    text="0"
)

etiquetaresultado.pack(padx=10,pady=10)















ventana.mainloop()

