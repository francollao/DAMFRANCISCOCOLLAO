class Persona:
    def __init__(self): #aqui tenemos la super clase
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.telefono = None
        self.edad = None
    def dameDatos(self):    #metodo
        print(
            "Nombre:",
            self.nombre,
            " - Apellidos:",
            self.apellidos,
            " - Email:",
            self.email,
            " - Teléfono:",
            self.telefono)
    def getNombre(self):    #getters y setters
        return self.nombre
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre

    def getEdad(self):
        return self.edad
    def setEdad(self,nuevaedad):
        if nuevaedad == self.edad + 1:
            self.edad = nuevaedad
        else:
            print("operación no permitida")
            
class Empleado(Persona):        #creamos una clase empleado que hereda de persona y una de cliente que tambien hereda de persona
    def __init__(self):
        super()

class Cliente(Persona):
    def __init__(self):
        super()

        #declaramos los objetos

cliente1 = Cliente()
cliente1.setNombre("Jantonio")
print(cliente1.getNombre())

empleado1 = Empleado()
empleado1.setNombre("pepe")
print(empleado1.getNombre())
    