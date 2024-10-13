import os
#sirve para trabajar con el sistema
try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe. Continuamos...")

while(True):
    print("Bienvenidos a mi diario v0.2")
    print("Seleciona una de las siguientes opciones")
    print("1. -Introducir un nuevo registro")
    print("2. -Leer registros existentes")


    opcion = input("Seleciona una opcion:")
    print("tu opcion ha sido: ",opcion)

    if opcion == "1":
        print("Has elegido introducir un nuevo registro")
        archivo = open("basededatos/midiario.txt",'a')
        fecha = input("seleciona la fecha: ")
        mensaje = input("Introduce el mensaje: ")
        archivo.write(fecha+"|"+mensaje+"\n")
        archivo.close()
    elif opcion == "2":
        print("Has elegido leer los registros")
        archivo = open("basededatos/midiario.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
    else:
        print("la opcion que has elegido no es válida")
