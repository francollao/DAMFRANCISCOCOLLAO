import mysql.connector

servidor = "localhost"          #creo variable que apunta mi servidor 
usuario = "expr"       #variable para almacenar mi usuario anteriormente creado
contrasena = "expr"    ##lo mismo con los siguientes datos 
base_de_datos = "expr"

conexion = mysql.connector.connect(     #establezco conexion con la bd con los datos anteriores
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
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
        peticion = "SELECT * FROM capitulos ; "                    # Pido todo de capitulos
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)          


    elif opcion == "2" :
        print("se va añadir un registro")
        cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        capitulo = input("Introduce el capitulo de este capitulo :")         # Le pido un nuevo Titulo al usuario
        titulo = input("Introduce el titulo del capítulo:")   # Le pido un nuevo Subtitulo al usuario
        subtitulo = input("Introduce el subtitulo del capítulo:")         # Le pido un nuevo Imagen al usuario
        videourl = input("Introduce el  url del Video del capítulo:")           # Le pido un nuevo Video al usuario
        descripcion = input("Introduce la descripcion del capítulo:")           # Le pido un nuevo Texto al usuario
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

        cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        id = input("Introduce el Identificador del capítulo a actualizar:")
        capitulo = input("Introduce el nuevo Titulo del capítulo (en blanco para no modificar):")        
        titulo = input("Introduce el nuevo Subtitulo del capítulo (en blanco para no modificar):")   
        subtitulo = input("Introduce el nuevo Imagen del capítulo (en blanco para no modificar):")        
        videourl = input("Introduce el nuevo Video del capítulo (en blanco para no modificar):")           
        descripcion = input("Introduce el nuevo Texto del capítulo (en blanco para no modificar):")           
        peticion = f"""
        UPDATE capitulos
        SET 
            capitulo = '{capitulo}',
            titulo  = '{titulo}',
            subtitulo = '{subtitulo}',
            videourl = '{videourl}',
            descripcion = '{descripcion}'
        WHERE
        id = {id}
        """                                 

        


    elif opcion == "4" :
        print("se va eliminar  un registro")

    elif opcion == "5" :
        print("Va a salir ")
        exit()

