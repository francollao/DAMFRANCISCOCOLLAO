class Gato:
    def __init__(self,nuevonombre,nuevaaltura,nuevopeso,nuevaedad): 
        self.altura = nuevaaltura
        self.edad = nuevaedad
        self.peso = nuevopeso
        self.nombre = nuevonombre  
    def maulla(self,numero): 
        cadena= " Miau " * numero 
        print(cadena)
    def estufera(self):
        print("ffffffffffff")

gatito = Gato("Micifu", 10,0.2,5)

print("El nombre del gato 1 es :",gatito.nombre)
print("la edad del gato es: ",gatito.edad)
