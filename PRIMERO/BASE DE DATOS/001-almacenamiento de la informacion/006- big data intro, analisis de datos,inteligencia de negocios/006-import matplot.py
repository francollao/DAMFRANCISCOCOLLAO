import matplotlib.pyplot as plt # type: ignore

etiquetas = ['Category A', 'Category B', 'Category C']
datos = [30, 45, 25]

plt.pie(datos, labels=etiquetas)

plt.savefig('grafica.png')

plt.close()