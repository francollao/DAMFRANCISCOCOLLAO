import time

inicio = time.time()

print(inicio)
iteraciones = 100000000
numero = 1.00000065
for i in range(0,iteraciones):
    numero *= 1.000000045
final = time.time()
print(final - inicio)