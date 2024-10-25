import sqlite3      #importamos la libreria de sqlite3, 
conexion =  sqlite3.connect('empresita.db')     #creamos conexion a sqlite3 y que cree una carpeta .bd 

cursor = conexion.cursor()      #creamos un cursor
                                #hacemos que el cursor ejecute el sql si no existe la tabla clientes en este caso
cursor.execute('''      
CREATE TABLE 
IF NOT EXISTS clientes
(
    identificador INTEGER PRIMARY KEY AUTOINCREMENT,        
    nombre TEXT,
    apellido TEXT,
    email TEXT,
    direccion TEXT     
               
               )

'''
            #declaramos las columnas de la tabla y que tipo van a ser 
)
                #ejecutamos de nuevo el cursor para insertar los valores a la tabla 
cursor.execute('''
    INSERT INTO clientes 
    VALUES(
        NULL,
        'Francisco',
        'Collao',
        'franciscojaviercollaocuellar@gmail.com', 
        'Calle de paquito'     
               
               
               )



'''
    #recordamos poner NULL al id ya que se va a autoincrementar por si mismo y ponemos los datos 

)

# haemos un commit, para que se envien esas sentencias 
conexion.commit()
    #realizamos un execute en el cual se hara una sentencia sql 
cursor.execute('''
    SELECT * FROM clientes;


'''
)

#almacenamos en filas todos los registros de la sentencia de sql 

filas = cursor.fetchall()
for fila in filas:      #hacemos un for de fila en todas las filas para que nos de todos los registros
    print(fila)     #la salida por pantalla de esto va ser entre parentesis en forma de tupla, es decir podriamos sacarlo de la siguiente forma fila[0], fila[1]

        # ahora se quiere actualizar de la tabla clientes el apellido a 'Alacaraz' donde el id sea el deseado por el usuario
cursor.execute('''
UPDATE clientes
SET apellidos = 'Alcaraz '
WHERE identificador = 1;

'''
#EN este execute vamos a borrar el cliente deseado por el cliente donde el usuario elija el identificador de usuario , mejor hacer input

)

cursor.execute('''
    DELETE FROM clientes
    WHERE identificador = 1;


'''


)

conexion.close()