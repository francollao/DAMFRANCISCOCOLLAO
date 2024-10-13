archivo = open("diario.txt",'r')
lineas = archivo.readlines()

for linea in lineas:
    print(linea)
