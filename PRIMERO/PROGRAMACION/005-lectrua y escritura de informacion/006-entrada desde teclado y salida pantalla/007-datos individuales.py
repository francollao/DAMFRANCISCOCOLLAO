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

peticion = "SELECT * from CLIENTES;"    #preparp peticion  xd era from, no form

cursor = conexion.cursor()  #una peticion en python requiere un cursor

cursor.execute(peticion)  #en el cursor,ejecuto la peticion
filas = cursor.fetchall()   #en una variable llamada filas almaceno los resultados que de la bdd
for fila in filas:
    #print(fila)     #como filas representa a todas las fila, quiero coger una a una
        #imprimo cada fila 
    print("########################")       # cada uno de los datos es un elemento de la coleccion de la tupla
    print("el id es: ", fila[0])
    print("el nombre es:", fila[1])
    print("el mail es:", fila[2])
    print("la poblacion es: ",fila[3])
    print("la fecha de nacimiento es: ",fila[4])