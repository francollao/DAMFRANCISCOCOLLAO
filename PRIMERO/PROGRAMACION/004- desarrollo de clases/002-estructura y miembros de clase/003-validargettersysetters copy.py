class Cliente:
     def __init__(self,nuevonombre,nuevosapellidos,nuevoemail,nuevotelefono,nuevaedad):
         
         self.nombre = nuevonombre
         self.apellidos = nuevosapellidos
         self.email = nuevoemail
         self.telefono = nuevotelefono
         self.edad = nuevaedad
         #atencion: no insertar el metodo dentro del constructor.
     def dameDatos(self):
             print("Nombre: ",self.nombre, "- Apellidos: ",self.apellidos,
                   "-telefono: ",self.telefono, "- Mail: ",self.email)
             
     def getNombre(self):
        return self.nombre

     def setNombre(self,nuevonombre):
        self.nombre = nuevonombre

     def getEdad(self):
        return self.edad

     def setEdad(self,nuevaedad):
         if nuevaedad == self.edad + 1:
            self.edad = nuevaedad
         else:
             print("operacion no permitida")
        





cliente1 = Cliente( "Fran","collao","francollao@gmail.com",656548654,20)

#cliente2 = Cliente( "pedro","Martinez","Pedromar@gmail.com", 654868498 )

print(cliente1.edad)
cliente1.setEdad(21)
print(cliente1.edad)
