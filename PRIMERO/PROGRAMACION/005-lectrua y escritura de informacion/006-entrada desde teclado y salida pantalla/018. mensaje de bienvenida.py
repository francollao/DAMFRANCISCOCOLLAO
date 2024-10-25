'''
Programa CRUD completo 
v0.1 Fran Collao
Objetivo es construir el CRUD completo contra MySQL


'''
import mysql.connector

servidor = "localhost"          #creo variable que apunta mi servidor 
usuario = "miempresa"       #variable para almacenar mi usuario anteriormente creado
contrasena = "miempresa"    ##lo mismo con los siguientes datos 
base_de_datos = "miempresa"

conexion = mysql.connector.connect(     #establezco conexion con la bd con los datos anteriores
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
)

print("############")
print("Prgrama CRUD completo")
print("############")
while True:
    print("selecciona una opcion: ")
    print("1. -Crear nuevo Cliente ")
    print("2. -Leer clientes existentes: ")
    print("3. -Actualizar cliente existente ")
    print("4. - Eliminar cliente ")
    print("5. - Salir del programa ")

    opcion = input("Selecciona una de las opciones")

    if opcion == "1":
        print("Vamos a crear un nuevo cliente")
        nombre = input("Introduce el nombre del nuevo cliente:")        # le pido todos los datos y los almacenos en una variable
        email = input("Introduce el mail del nuevo cliente:")
        poblacion = input("Introduce la pobalcion del nuevo cliente:")
        fechadenacimiento = input("Introduce la fecha de nacimento del nuevo cliente:")
        peticion = "INSERT INTO clientes VALUES (NULL,'','','','');"    #preparp peticion
        
        cursor = conexion.cursor()  #una peticion en python requiere un cursor
        cursor.execute(peticion)
        conexion.commit()
    elif opcion =="2":
        print("Vamos a leer los clientes")

    elif opcion =="3":
        print("Vamos a actualizar clientes")
    elif opcion =="4":
        print("Vamos a eliminar un cliente ")
    elif opcion =="5":
        exit()

    else:
        print("LA OPCION QUE HAS ESCOGIDO ES INCORRECTA")