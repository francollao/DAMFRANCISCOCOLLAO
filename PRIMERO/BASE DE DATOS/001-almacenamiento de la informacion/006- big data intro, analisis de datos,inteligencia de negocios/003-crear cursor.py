import sqlite3

conexion = sqlite3.connect('registros (1).db')

cursor = conexion.cursor()

cursor.execute('''
    SELECT * FROM logs;
''')                                                           
filas = cursor.fetchall()                                      
for fila in filas:                                              
    print(fila) 

    #so lo ejecuto me muero esperando