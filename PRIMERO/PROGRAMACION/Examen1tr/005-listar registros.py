import mysql.connector

'''
    Examen hecho por Fran Collao de programacion



'''

conexion = mysql.connector.connect(
    host="localhost",           
    user="examenprog",        
    password="examenprog",   
    database="examenprog"    
)          


#hacemos el menu


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
        cursor = conexion.cursor(dictionary = True)             # Creo un cursor y me aseguro de que la info me viene en JSON
        peticion = "SELECT * FROM capitulos"                    # Pido todo de capitulos
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)          


    elif opcion == "2" :
        print("se va añadir un registro")
        cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        capitulo = input("Introduce el Titulo del capítulo:")         # Le pido un nuevo Titulo al usuario
        titulo = input("Introduce el Subtitulo del capítulo:")   # Le pido un nuevo Subtitulo al usuario
        subtitulo = input("Introduce el Imagen del capítulo:")         # Le pido un nuevo Imagen al usuario
        videourl = input("Introduce el Video del capítulo:")           # Le pido un nuevo Video al usuario
        descripcion = input("Introduce el Texto del capítulo:")           # Le pido un nuevo Texto al usuario
        peticion = f"""
        INSERT INTO capitulos
        VALUES (
            NULL,
            '{capitulo}',
            '{titulo}',
            '{subtitulo}',
            '{videourl}',
            '{descripcion}'
        )"""                     

    elif opcion == "3" :
        print("se va actualizar un registro")

       



    elif opcion == "4" :
        print("se va eliminar  un registro")




    elif opcion == "5" :
        print("Va a salir ")
        exit()

