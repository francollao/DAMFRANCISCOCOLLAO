import mysql.connector

class ConectorBD:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database = 'practicaprog',
            user = 'praticaprog',
            password = ''

        )
        self.cursor = self.conexion.cursor(dictionary = True)

    def dameTablas(self):#hay que poner self como parametro base
      
        peticion = "SHOW TABLES; "

        self.cursor.execute(peticion)

        registros = self.cursor.fetchall()

        return registros

    def leerTabla(self,tabla): #hay que poner self como parametro base

        peticion = "SELECT * FROM  " +tabla

        self.cursor.execute(peticion)

        registros = self.cursor.fetchall()

        return registros
    

    def insertaTabla(self):
    
        pass 
    

    def actualizaTabla(self):
        pass

    def eliminaTabla(self):
        pass

    

#creamo el objeto de la clase :
