import sqlite3
import matplotlib.pyplot as plt

conexion = sqlite3.connect('registros (1).db')
conexion.text_factory = lambda x: str(x, 'utf-8', 'replace')
cursor = conexion.cursor()

cursor.execute('''
    SELECT
    COUNT(anio) as año,
    anio
    FROM logs
    GROUP BY anio
    ;
''')

filas = cursor.fetchall()

etiquetas = []
datos = []

for fila in filas:                                              
    etiquetas.append(fila[1])
    datos.append(fila[0])


plt.pie(datos, labels=etiquetas)

plt.savefig('bigdata.png')

plt.close()