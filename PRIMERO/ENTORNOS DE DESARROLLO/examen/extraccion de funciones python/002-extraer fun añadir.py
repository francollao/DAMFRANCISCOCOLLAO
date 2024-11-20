'''
Programa CRUD completo 
v0.1 Fran Collao
Objetivo es construir el CRUD completo contra MySQL


'''


import mysql.connector


servidor = "localhost"          #creo variable que apunta mi servidor 
usuario = "expr"       #variable para almacenar mi usuario anteriormente creado
contrasena = "expr"    ##lo mismo con los siguientes datos          SE HABIA RAYADO XAMPP O ALGO POR QUE NO ME DEJABA HACER NADA CON LA BDD
base_de_datos = "expr"

conexion = mysql.connector.connect(     #establezco conexion con la bd con los datos anteriores
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
)
#hacemos el menu

#vamos a extraer las funciones para que el codigo sea mas simple y sencillo.



def seleccionaCapitulo():
    cursor = conexion.cursor(dictionary = True)             # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = "SELECT * FROM capitulos"                    # Pido todo de capitulos
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    return filas                                            # Imprimo las filas


#lo que se va devolver en esta funcion va ser el selecct de la peticion que es ejeutado y almacenado en filas


#funcion para añadir un nuevo registro 


def insertaCapitulo():
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
    capitulo = input("Introduce el capitulo del capítulo:")         # Le pido un nuevo Titulo al usuario
    titulo = input("Introduce el titulo del capítulo:")   # Le pido un nuevo Subtitulo al usuario
    subtitulo = input("Introduce el subtitulo del capítulo:")         # Le pido un nuevo Imagen al usuario
    videourl = input("Introduce el url Video del capítulo:")           # Le pido un nuevo Video al usuario
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
    )"""                                                    # Inserto un nuevo capítulo
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    conexion.commit()
    return True





while True:
    print("#########")
    print("Elija una opcion de las siguientes: ")           #hacemos un menu que saldra constantemente para realizar las diferentes opciones 
    print("1.- Listar registros")
    print("2.- Añadir Regsitros")
    print("3.- Actualizar Registro")
    print("4.- Eliminar Registro")
    print("5.- Salir")

    opcion = input("Seleccion la opcion: ")             #capturamos la opcion 




    if opcion == "1":
        print("Se van a listar los registros")
        print(seleccionaCapitulo()) #metemos la funncion dentro de un print para que nos devuelva por pantalla, por que sino la lllamarios pero no hariamos nada
        


    elif opcion == "2":
        print(insertaCapitulo())  #llamamos a la funcion y borramos lo que teniamos escrito en esta apartado ya que la funcion lo sustituye
          

    elif opcion == "3":
        print("se va actualizar un registro")

        cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        id = input("Introduce el Identificador del capítulo a actualizar:")
        capitulo = input("Introduce el nuevo capitilo de los capitulos (en blanco para no modificar):")        
        titulo = input("Introduce el nuevo titulo del capítulo (en blanco para no modificar):")   
        subtitulo = input("Introduce el nuevo subtitulo capítulo (en blanco para no modificar):")        
        videourl = input("Introduce el nuevo Video del capítulo (en blanco para no modificar):")           
        descripcion = input("Introduce la nueva descripcion  del capítulo (en blanco para no modificar):")           
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
        ; """               
        conexion.commit()                  

        


    elif opcion == "4":
        print("se va eliminar  un registro")

        cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
        Identificador = input("Introduce el Identificador del capítulo a eliminar:")         # Le pido un nuevo Titulo al usuario
        peticion = f"""
        DELETE FROM capitulos
        WHERE id = {id}
       ;  """     
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        print(filas)                                            # Imprimo las filas
        conexion.commit()           #commit para que se quede guardado

    elif opcion == "5":
        print("Va a salir ")
        exit()

