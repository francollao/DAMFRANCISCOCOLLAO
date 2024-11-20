
class Cliente:
    def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail

class Productos:
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.descripcion = nuevadescripcion
        self.precio = nuevoprecio

clientes = []
productos = [] ##creamos una lista

print("Programa de Consola")
print("v0.1 por Franc collao")

print("Selecciona entidad")
print("1.-Clientes")
print("2.-Productos")

entidad = input("Indica la opcion seleccionada:")


print("Selecciona operacion")
print("1.-Insertar un nuevo registro")
print("2.-Listar registros")
print("3.-Actualizar registro")
print("4.-Eliminar registro")