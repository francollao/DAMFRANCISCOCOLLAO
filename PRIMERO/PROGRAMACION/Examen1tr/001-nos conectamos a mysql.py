import mysql.connector

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

