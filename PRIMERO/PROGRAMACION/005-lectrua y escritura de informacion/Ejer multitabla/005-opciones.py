import mysql.connector

connection = mysql.connector.connect(
    host='localhost',   
    user='miempresa',   
    password='miempresa',
    database='miempresa' 
)
cursor = connection.cursor() #NO ME INTERESA, SE VE DIFERENTE

print("Programa de gestión de empresa v0.0")
print("Fran Collao")

print("Selecciona una tabla de la base de datos: ")
peticion="SHOW TABLES;"

cursor.execute(peticion)
filas = cursor.fetchall()
tablas= []
for fila in filas:
    tablas.append(fila[0])  # ponemos esto, para que en la lista tabla se almacene 
                            # el primer y unico elemento de la tupla que es 0, por eso fila[0] añadido a lista tabla

contador = 0
for tabla in tablas:
    print(contador,"-",tabla)
    contador += 1

opcion = input("Selecciona una tabla: ")
print("se va a trabajar con la tabla: ",tablas[int(opcion)])
print("la peticion que voy a lanzar a la base de datos es: ",peticion)
peticion = "SELECT * FROM ",tablas[int(opcion)]

print("1- Introduce nuevo ",tablas[int(opcion)], ":")
print("2- Listar ",tablas[int(opcion)], ":")
print("3- Actualizar ",tablas[int(opcion)], ":")
print("4- Eliminar ",tablas[int(opcion)], ":")
opcion2 = input("Selecciona una opcion: ")

if opcion2 =="1":
    print("Vamos a insertar un nuevo ",tablas[int(opcion)])

elif opcion2 == "2":
    print("Vamos a listar: ",tablas[int(opcion)])
    peticion = "SELECT * FROM "+tablas[int(opcion)]
    cursor.execute(peticion)
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


elif opcion2 == "3":
    print("Vamos a Actualizar: ",tablas[int(opcion)])


elif opcion2 =="4":
    print("Vamos a eliminar: ",tablas[int(opcion)])




