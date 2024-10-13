
print("Mi diario v0.1")
fecha = input("Introduce fecha de entrada")
mensaje = input("Introduce lo que ha pasado hoy ")


archivo = open("diario.txt",'a')
archivo.write(fecha+"|"+mensaje+"\n")

archivo.close()
