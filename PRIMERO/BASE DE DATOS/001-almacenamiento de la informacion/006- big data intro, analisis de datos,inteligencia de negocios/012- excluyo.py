import sqlite3

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
#excluyo a españa
filas = cursor.fetchall()


for fila in filas:
    print(fila)