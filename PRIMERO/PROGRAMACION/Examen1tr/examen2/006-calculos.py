'''
Programa de base IVA e IRPF


FRAN COLLAO

'''


import tkinter as tk        #importamos tk inter como tk

ventana = tk.Tk() #creamos la ventana 
ventana.geometry("600x600+200+200")         #le damos las dimensiones y el bordeado de las esquinas 
ventana.title("EXAMEN DE PROGRAMACION")         #ponemos titulo a la ventana

baseimpo = tk.IntVar() #almacenamos la variable en formato de numero ya que el tipo de dato es un numero

#creamos una funcion para que nos calcule el IVA y el IRPF

def iva():
    global ivaresul
    global irpfresul
    global resulfinal

    print("calculamos iva")
    iva1 =baseimpo.get()
    ivacalculo = (iva1 * 21/100)
    ivaresul.config(text=str(ivacalculo)) ## para que la salida por pantalla sea en formato de texto


    print("calcularemos el irpf")
    irpf1 = baseimpo.get()
    irpfcalculo = (irpf1 * 15/100) 
    irpfresul.config(text=str(irpfcalculo))

    print("calculamos resultado final")
    basefinal = baseimpo.get()
    finalcalculo = basefinal - ( basefinal * 15/100) + (basefinal * 21/100)
    resulfinal.config(text=str(finalcalculo))




'''
def irpf():
    global irpfesul
    print("calcularemos el irpf")
    irpf1 = baseimpo.get()
    irpfcalculo = irpf1 * 15/100
    irpfresul.config(text=str(irpfcalculo))'''






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
          text="SABRAS LOS DATOS",
          command=iva
              
).pack(padx=15,pady=15)







tk.Label(ventana,           #creamos etiqueta para resultado DEL IVA 
    text="los resultados IVA son: "

).pack(padx=15,pady=15)


ivaresul= tk.Label(ventana,
                   text="0"

)

ivaresul.pack(padx=15,pady=15)

##CREMO OTRA EIQUETA PARA EL RESULTADO DEL IRPF

tk.Label(ventana,         
    text="los resultados con IRPF son: "

).pack(padx=15,pady=15)


irpfresul= tk.Label(ventana,
                   text="0"

)

irpfresul.pack(padx=15,pady=15)

##CREAMOS LA FACTURA TOTAL 


tk.Label(ventana,         
    text="los resultado final es:  "

).pack(padx=15,pady=15)


resulfinal= tk.Label(ventana,
                   text="0"

)

resulfinal.pack(padx=15,pady=15)


'''
ivaresul.pack(padx=15,pady=15)
irpfresul.pack(padx=15,pady=15)
resulfinal.pack(padx=15,pady=15)'''



ventana.mainloop()      #con esto hacemos que la ventana salga por pantalla y sea visible 

