import sqlite3
import matplotlib.pyplot as plt

# Conectar a la base de datos
conexion = sqlite3.connect('registros (1).db')
conexion.text_factory = lambda x: str(x, 'utf-8', 'replace')
cursor = conexion.cursor()

# Ejecutar consulta SQL
cursor.execute('''
    SELECT
    COUNT(extra3) as numero,
    extra3
    FROM logs
    WHERE (
        extra3 != ''
        AND
        extra3 != 'es'
    )
    GROUP BY extra3
    ORDER BY numero DESC
    LIMIT 20
    ;
''')

filas = cursor.fetchall()

etiquetas = []
datos = []

for fila in filas:
    etiquetas.append(fila[1])
    datos.append(fila[0])

plt.pie(datos, labels=etiquetas)

plt.savefig('paises.png')

plt.close()