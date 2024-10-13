import os
#sirve para trabajar con el sistema
try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe. Continuamos...")

