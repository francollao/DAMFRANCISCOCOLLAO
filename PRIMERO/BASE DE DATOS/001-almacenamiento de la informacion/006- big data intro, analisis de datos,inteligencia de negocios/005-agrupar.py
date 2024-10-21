import sqlite3

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
''')                          #agrupamos por le año para que no nos salgan todos los datos                                 
filas = cursor.fetchall()                                      
for fila in filas:                                              
    print(fila) 