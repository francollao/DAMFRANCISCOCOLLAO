
'''
    Programa calculadora de primer tema de clase
    (c) 2024 Fran Collao
    Este programa está hecho en Python :)
'''

# presentacion 

NOMBRE_DEL_PROGRAMA = "Programa calculadora"
VERSION = "0.1"
AUTOR = "FRAN COLLAO "
print(NOMBRE_DEL_PROGRAMA,VERSION,AUTOR)




#toma de datos 

print ("Programa Calculadora")

operando1 = input("Introduce el primer operando")
operando2 = input("Introduce el segundo operando")
operador = input("Introduce el segundo operador (+-*/)")
#conversiones de los datos a tratar 


operando1 = int(operando1)
operando2 = int(operando2)
#toma de deciciones segun el usuario desee
if operador == "+":
    resultado = operando1 + operando2
elif operador == "-":
    resultado = operando1 - operando2
elif operador == "*":
    resultado = operando1 * operando2
elif operador == "/":
    resultado = operando1 / operando2
#salida del resultado elegido por pantalla 
print("El resultado de la operación es:", resultado)
       
'''
esto es una calculadora en el cual utilizamos la estructura if y comparadores  para comprobar que opcion se ha elegido


'''