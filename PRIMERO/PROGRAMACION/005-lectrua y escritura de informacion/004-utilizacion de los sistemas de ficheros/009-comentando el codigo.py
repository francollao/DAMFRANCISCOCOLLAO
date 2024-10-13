import os           #importamos libreria
#sirve para trabajar con el sistema
try:                # metemos un try expect, por si ya esta creado, no se pare el programa
                    # y no de error,sino se crea y ya
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe. Continuamos...")
            #añadimos la excepcion

while(True):        #hacemos bucle infinito
                    #hacemos un pequeño menu para el usuario para que sepa que opciones
                    #tiene para hacer en este programa
    print("Bienvenidos a mi diario v0.2")
    print("Seleciona una de las siguientes opciones")
    print("1. -Introducir un nuevo registro")
    print("2. -Leer registros existentes")

            #atrapo la opcion que ha elegido y la meto en una variable
    opcion = input("Seleciona una opcion:")
    print("tu opcion ha sido: ",opcion)
     #le indicamos que opcion ha elegido
    
    #si la opcion introducida no 1 o 2 entonces comunicamos que no es valida
    
    #en caso de que si sea valida se comrpueba que tipo de tarea tiene que realizar

    if opcion == "1":
        print("Has elegido introducir un nuevo registro")
        archivo = open("basededatos/midiario.txt",'a')
        fecha = input("seleciona la fecha: ")
        mensaje = input("Introduce el mensaje: ")
        archivo.write(fecha+"|"+mensaje+"\n")
        archivo.close()
#si la opcion es escribir entonces: creamos o abrimos archivo y preguntamos
#la fecha y el mensaje a escribir que se almacenaran en sus respectivas variables
        
    elif opcion == "2":
        print("Has elegido leer los registros")
        archivo = open("basededatos/midiario.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)

#si la opcion es leer entonces: abrimos el archivo pero esta vez en lectura
#cargo las lineas del archivo y se las muestro al usuario en lineas independientes
    else:
        print("la opcion que has elegido no es válida")
