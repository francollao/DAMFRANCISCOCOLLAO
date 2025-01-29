from  ConectorBD import *  #NO PODEMOS PONER 005 Y EL NOMBRE, TIENE QUE SER PURO

conexion1 = ConectorBD()
print("programa de empresa: ")
print("FRan collao")

while True:
    tablas = conexion1.dameTablas()

    for tabla in tablas:
        print(str(tablas.index(tabla)+1) + " - " +tabla['Tables_in_practicaprog'])

    opcion = input("selecciona una tabla: ")

    print("has seleccionado: " +opcion)
    print("Vamos a trabajar con la tabla: "+tablas[int(opcion)-1]['Tables_in_practicaprog'])


    print("Ahora escoje una opcion ")
    print("1.- Insertar Regaitros")
    print("2.- Listar Regaitros")
    print("3.- Actualizar Regaitros")
    print("4.- Eliminar Regaitros")

    opcion2 = input("Selecciona que operacion quiere realizar")

    if opcion2 == "1":
        print("Vamos a insertar un registro")
    elif opcion2 =="2":
        print("Vamos a listar: ")
        print(conexion1.leerTabla(tablas[int(opcion)-1]['Tables_in_practicaprog']))

    elif opcion2 == "3":
        print("Actualizaremos registro: ")


    elif opcion2 == "4":
        print("Eliminaremos registro: ")