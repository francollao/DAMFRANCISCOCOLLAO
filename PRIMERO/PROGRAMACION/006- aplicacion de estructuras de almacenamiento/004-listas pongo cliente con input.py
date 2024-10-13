clientes = []

clientes.append("Fran")
print(clientes)
clientes.append("pepe")
print(clientes)

while(True):
    nombre = input("Introduce nombre de nuevo cliente: ")
    clientes.append(nombre)
    print(clientes)
    # print(clientes[2]) de esta forma solo imprime el elemento que se encuentra
    # en esa posicion, teniendo en cuenta que el primer elemento es 0
