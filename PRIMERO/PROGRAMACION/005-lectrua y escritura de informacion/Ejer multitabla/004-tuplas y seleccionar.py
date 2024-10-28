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
    contador =+1

