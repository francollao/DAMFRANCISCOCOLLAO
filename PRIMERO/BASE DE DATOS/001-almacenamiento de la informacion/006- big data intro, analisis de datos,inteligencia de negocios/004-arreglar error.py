import sqlite3

conexion = sqlite3.connect('registros (1).db')
conexion.text_factory = lambda x: str(x, 'utf-8', 'replace') #para corregir el error de utf-8
cursor = conexion.cursor()

cursor.execute('''
    SELECT * FROM logs;
''')                                                           
filas = cursor.fetchall()                                      
for fila in filas:                                              
    print(fila) 