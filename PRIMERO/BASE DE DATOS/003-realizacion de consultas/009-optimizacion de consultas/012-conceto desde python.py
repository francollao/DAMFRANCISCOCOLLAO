import mysql.connector

print("###############################")
print("FACTURA")
print("###############################")

servidor:"localhost"
usuario:"miempresa"
contrasena:"miempresa"
base_de_datos="miempresa"

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)       

pedido=2

peticion = '''SELECT clientes.nombre,clientes.email,clientes.poblacion FROM pedidos 
LEFT JOIN clientes 
ON pedidos.cliente_nombre = clientes.id WHERE pedidos.id = 2;'''

cursor = conexion.cursor()                      # Una petición en Python requiere un cursor

cursor.execute(peticion)                        # En el cursor, ejecuto la petición que he dejado preparada arriba
filas = cursor.fetchall()               
for fila in filas:
    print(fila)