import mysql.connector
from flask import Flask #importamos libreria que permite crear miniservidor web
aplicacion = Flask(__name__) #creo servidor web

servidor = "localhost"          #creo variable que apunta mi servidor 
usuario = "ex"       #variable para almacenar mi usuario anteriormente creado
contrasena = "miempresa"    ##lo mismo con los siguientes datos 
base_de_datos = "miempresa"

conexion = mysql.connector.connect(     #establezco conexion con la bd con los datos anteriores
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
)

@aplicacion.route('/')                          #creo escuchador para que este pendiente cuando alguien entre en la raiz
def inicio():                                    #defino funcion
    peticion = "SELECT * from CLIENTES;"    #preparp peticion


    cursor = conexion.cursor()                  #una peticion en python requiere un cursor

    cursor.execute(peticion)                    #en el cursor,ejecuto la peticion
    conetido=[]
    filas = cursor.fetchall()                 #en una variable llamada filas almaceno los resultados que de la bdd
    for fila in filas:
        conetido.append(fila)
    return conetido                        #como filas representa a todas las fila, quiero coger una a una
                                            #imprimo cada fila 

aplicacion.run(debug=True)                   #arranco el servidor 