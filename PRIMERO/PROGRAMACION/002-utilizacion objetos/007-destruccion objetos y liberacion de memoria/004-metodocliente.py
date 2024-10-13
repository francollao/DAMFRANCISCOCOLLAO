class Cliente:
     def __init__(self,nuevonombre,nuevosapellidos,nuevoemail,nuevotelefono):
         
         self.nombre = nuevonombre
         self.apellidos = nuevosapellidos
         self.email = nuevoemail
         self.telefono = nuevotelefono
         #atencion: no insertar el metodo dentro del constructor.
         

     def dameDatos(self):
             print("Nombre: ",self.nombre, "- Apellidos: ",self.apellidos,
                   "-telefono: ",self.telefono, "- Mail: ",self.email)





cliente1 = Cliente( "Fran","collao","francollao@gmail.com",656548654 )

cliente2 = Cliente( "pedro","Martinez","Pedromar@gmail.com", 654868498 )

cliente1.dameDatos()
cliente2.dameDatos()

print(cliente1)
cliente1 = None  # como hemos dicho antes esto sirve para destruir el obj
print(cliente1)
