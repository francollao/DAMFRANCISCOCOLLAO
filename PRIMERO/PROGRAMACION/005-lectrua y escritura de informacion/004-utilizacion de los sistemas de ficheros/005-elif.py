import os
#sirve para trabajar con el sistema
try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe. Continuamos...")


print("Bienvenidos a mi diario v0.2")
print("Seleciona una de las siguientes opciones")
print("1. -Introducir un nuevo registro")
print("2. -Leer registros existentes")


opcion = input("Seleciona una opcion:")
print("tu opcion ha sido: ",opcion)

if opcion == "1":
    print("Has elegido introducir un nuevo registro")


    
elif opcion == "2":
    print("Has elegido leer los registros")
else:
    print("la opcion que has elegido no es válida")
