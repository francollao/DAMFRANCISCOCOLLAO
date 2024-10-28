import mysql.connector

connection = mysql.connector.connect(
    host='localhost',   
    user='miempresa',   
    password='miempresa',
    database='miempresa' 
)
cursor = connection.cursor(dictionary=True)

print("Programa de gestión de empresa v0.0")
print("Fran Collao")

print("Selecciona una tabla de la base de datos: ")
peticion="SHOW TABLES;"