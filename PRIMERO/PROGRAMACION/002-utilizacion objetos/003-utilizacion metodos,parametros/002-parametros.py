class Gato:
    def __int___(self): #definir la plantilla de un gato que esta vacia
        self.altura = None
        self.edad = None
        self.peso = None
    

    def maulla(self,numero): #añadimos un parametro
        cadena= " Miau " * numero 
        print(cadena)
    def estufera(self):
        print("ffffffffffff")


gato1 = Gato()

gato1.maulla(25)#indicamos cual va ser el parametro
gato1.estufera()
