
import pickle

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

while True:

    print("Selecciona entidad")
    print("1.-Clientes")
    print("2.-Productos")

    entidad = input("Indica la opcion seleccionada:")


    print("Selecciona operacion")
    print("1.-Insertar un nuevo registro")
    print("2.-Listar registros")
    print("3.-Actualizar registro")
    print("4.-Eliminar registro")
    print("5.-Guardar")
    print("6.-Cargar")

    opcion = input("Selecciona una de estas operaciones:")

    if opcion == "1":
        print("Insertamos un nuevo registro")                                    # Imprimo un mensaje
        identificador = input("Introduce el id del nuevo cliente: ")                  # Introduzco los datos que pido para la clase
        nombre = input("Introduce el nombre del nuevo cliente: ")
        apellidos = input("Introduce los apellidos del nuevo cliente: ")
        email = input("Introduce el email del nuevo cliente: ")
        clientes.append(Cliente(identificador,nombre,apellidos,email)) 



    elif opcion == "2":
        print("Listamos los registros")
        for cliente in clientes:                                                    # Para cada uno de los clientes en la lista de clientes
            print("------------------")                                             # Pongo un separador
            print("id: "+cliente.identificador)                                     # Imprimo cada una de las caracteristicas
            print("nombre: "+cliente.nombre)
            print("apellidos: "+cliente.apellidos)
            print("email: "+cliente.email)
            

    
    elif opcion == "3":
        print("Actualizamos los registros")
        idlista = input("Selecciona el elemento de la lista de Python que quieres actualizar:")
        identificador = input("Introduce el id del cliente modificado: ")                  # Introduzco los datos que pido para la clase
        nombre = input("Introduce el nombre del cliente modificado: ")
        apellidos = input("Introduce los apellidos del cliente modificado: ")
        email = input("Introduce el email del cliente modificado ")
        clientes[int(idlista)].identificador = identificador
        clientes[int(idlista)].nombre = nombre
        clientes[int(idlista)].apellidos = apellidos
        clientes[int(idlista)].email = email


    elif opcion == "4":
        print("Eliminamos registros")
        idlista = input("Selecciona el elemento de la lista de Python que quieres eliminar:")
        clientes.pop(int(idlista))
    
    elif opcion == "5":
        archivo = open("clientes.dat",'wb')
        pickle.dump(clientes,archivo)
        archivo.close()

    elif opcion == "6":
        archivo = open("clientes.dat",'rb')
        clientes = pickle.load(archivo)
        archivo.close()