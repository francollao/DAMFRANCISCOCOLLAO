import mysql.connector

'''
    Examen hecho por Fran Collao de programacion



'''


servidor = "localhost"          #creo variable que apunta mi servidor 
usuario = "examenprog"       #variable para almacenar mi usuario anteriormente creado
contrasena = "examenprog"    ##lo mismo con los siguientes datos 
base_de_datos = "examenprog"

conexion = mysql.connector.connect(     #establezco conexion con la bd con los datos anteriores
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
)
#hacemos el menu
cursor = conexion.cursor(dictionary=True) #nos lo va devolver en formato json


while True:
    print("#########")
    print("Elija una opcion de las siguientes: ")
    print("1.- Listar registros")
    print("2.- Añadir Regsitros")
    print("3.- Actualizar Registro")
    print("4.- Eliminar Registro")
    print("5.- Salir")

    opcion = input("Seleccion la opcion: ")


    if opcion == "1":
        print("Se van a listar los registros")


    elif opcion == "2" :
        print("se va añadir un registro")


    elif opcion == "3" :
        print("se va actualizar un registro")


    elif opcion == "4" :
        print("se va eliminar  un registro")

    elif opcion == "5" :
        print("Va a salir ")
        exit()

