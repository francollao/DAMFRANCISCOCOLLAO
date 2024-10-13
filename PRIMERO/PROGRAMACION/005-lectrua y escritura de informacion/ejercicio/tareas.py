
'''

FRAN COLLAO ℗ 
PROGRAMA PARA VER TUS TAREAS IMPORTANTES 




'''


import os
try:
    os.makedirs("TareasSemanales")
except:
    print(" la carpeta ya existe")


while(True):
    print("Bienvenidos a Agenda Personal0.1")
    print("****Seleciona una de las siguientes opciones****")
    print("1. -Introducir Acontecimiento")
    print("2. -Leer Acontecimientos de día")

    opcion = input("Selecione una opcion: ")


    if opcion == "1":
        print("Has elegido añadir acontecimiento: ")
        print("en que dia desea añadirlo: ")
        print("1---LUNES---")
        print("2---MARTES---")
        print("3---MIERCOLES---")
        print("4---JUEVES---")
        print("5---VIERNES---")

        dia = input("eliga el dia, indicando el numero que le corresponde: ")

        if dia == "1":
            archivo = open("TareasSemanales/lunes.txt",'a')
            acontecimiento = input("introduzca el acontecimiento: ")
            fecha = input("seleciona la fecha: ")
            mensaje = input("Introduce el mensaje: ")
            archivo.write(fecha+"|"+"**"+acontecimiento+"***"+mensaje+"\n")
            archivo.close()
        elif dia == "2":
            archivo = open("TareasSemanales/martes.txt",'a')
            acontecimiento = input("introduzca el acontecimiento: ")
            fecha = input("seleciona la fecha: ")
            mensaje = input("Introduce el mensaje: ")
            archivo.write(fecha+"|"+"**"+acontecimiento+"***"+mensaje+"\n")
            archivo.close()
            
        elif dia == "3":
            archivo = open("TareasSemanales/miercoles.txt",'a')
            acontecimiento = input("introduzca el acontecimiento: ")
            fecha = input("seleciona la fecha: ")
            mensaje = input("Introduce el mensaje: ")
            archivo.write(fecha+"|"+"**"+acontecimiento+"***"+mensaje+"\n")
            archivo.close()
        elif dia == "4":
            archivo = open("TareasSemanales/jueves.txt",'a')
            acontecimiento = input("introduzca el acontecimiento: ")
            fecha = input("seleciona la fecha: ")
            mensaje = input("Introduce el mensaje: ")
            archivo.write(fecha+"|"+"**"+acontecimiento+"***"+mensaje+"\n")
            archivo.close()
        elif dia == "5":
            archivo = open("TareasSemanales/viernes.txt",'a')
            acontecimiento = input("introduzca el acontecimiento: ")
            fecha = input("seleciona la fecha: ")
            mensaje = input("Introduce el mensaje: ")
            archivo.write(fecha+"|"+"**"+acontecimiento+"***"+mensaje+"\n")
            archivo.close()
        else: 
             print("Ese numero no esta disponible")


        



    elif opcion == "2":
        print("*******Has elegido leer tu agenda ********")
        print("¿QUE DIA DESEES LEER? ")
        print("1---LUNES---")
        print("2---MARTES---")
        print("3---MIERCOLES---")
        print("4---JUEVES---")
        print("5---VIERNES---")
        dia = input("eliga el dia, indicando el numero que le corresponde: ")

        if dia == "1":
            try:
                print("***SE VAN A MOSTRAR ACONTECIMIENTOS DE LUNES***")
                archivo = open("TareasSemanales/lunes.txt",'r')
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea)
            except:
                print("No Hay nada planificado para este dia")
        elif dia == "2":
            try:
                print("***SE VAN A MOSTRAR ACONTECIMIENTOS DE MARTES***")
                archivo = open("TareasSemanales/martes.txt",'r')
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea)
            except:
                print("No Hay nada planificado para este dia")
            
        elif dia == "3":
            try:
                print("***SE VAN A MOSTRAR ACONTECIMIENTOS DE MIERCOLES***")
                archivo = open("TareasSemanales/miercoles.txt",'r')
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea)
            except:
                print("No Hay nada planificado para este dia")
        elif dia == "4":
            try:
                print("***SE VAN A MOSTRAR ACONTECIMIENTOS DE JUEVES***")
                archivo = open("TareasSemanales/jueves.txt",'r')
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea)
            except:
                print("No Hay nada planificado para este dia")
        elif dia == "5":
            try:
                print("***SE VAN A MOSTRAR ACONTECIMIENTOS DE VIERNES***")
                archivo = open("TareasSemanales/viernes.txt",'r')
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea)
            except:
                print("No Hay nada planificado para este dia")
        else: 
             print("Ese numero no esta disponible")
     

    else:
            print("la opcion que has elegido no es válida")

    
