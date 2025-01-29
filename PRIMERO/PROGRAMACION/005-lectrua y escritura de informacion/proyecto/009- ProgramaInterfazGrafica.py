from ConectorBD import *
import tkinter as tk

conexion1 = ConectorBD()

ventana = tk.Tk()
tablas = conexion1.dameTablas()

for tabla in tablas:
    tk.Button(ventana,text=tabla['Tables_in_practicaprog']).pack(padx=15,pady=15)



ventana.mainloop()