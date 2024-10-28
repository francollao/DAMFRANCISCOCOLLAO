import tkinter as tk
ventana = tk.Tk()

ventana.geometry("500x500+150+150")
ventana.title("La Calculadora de Fran Collao")

operando1 = tk.IntVar()
operando2 = tk.IntVar()


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
    textvariable=operando1
).pack(padx=10,pady=10)
tk.Label(
    ventana,
    text="pulsa para obtener resutado "
).pack(padx=10,pady=10)
tk.Label(
    ventana,
    text="El resultado es:  "
).pack(padx=10,pady=10)














ventana.mainloop()

