import mysql.connector
def dameTablas():
    conexion = mysql.connector.connect(
        host='localhost',
        database = 'practicaprog',
        user = 'praticaprog',
        password = ''

    )

    cursor = conexion.cursor(dictionary = True)
    peticion = "SHOW TABLES; "

    cursor.execute(peticion)

    registros = cursor.fetchall()

    return(registros)

def leerTabla():
    conexion = mysql.connector.connect(
        host='localhost',
        database = 'practicaprog',
        user = 'praticaprog',
        password = ''

    )

    cursor = conexion.cursor(dictionary = True)
    peticion = "SELECT * FROM CLIENTES; "

    cursor.execute(peticion)

    registros = cursor.fetchall()

    return(registros)




print(dameTablas()) #esto pasa por que una funcion devuelve algo, por eso hacemos print de la funcion
print(leerTabla())