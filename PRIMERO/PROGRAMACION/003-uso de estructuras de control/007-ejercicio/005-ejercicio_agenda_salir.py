'''
    Programa agenda
    (c) 2024 Fran collao

'''

TITULO = "PROGRAMA AGENDA"
AUTOR = "FRAN COLLAO"


print(TITULO,"por",AUTOR)


#ESTRUCUTURA DE EJECUCION INFINITA ############

while(True):

    #Menu principal #######################

    print("Escoge una opcion")
    print("1.- Insertar")
    print("2.- Listar")
    print("3.- Actualizar")
    print("4.- Eliminar")
    print("5.- Salir")
    # el usuario escoge una opcion ####################
    opcion = input("Seleciona una opcion (1-5)")
    print("Has selecionado la opcion: ",opcion)

    ## seleciono la operacion a realizar############

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
    elif opcion == "2":
        print("Vamos a listar cliente")
    elif opcion == "3":
        print("Vamos a actualiras un cliente")
    elif opcion == "4":
        print("Vamos a eliminar un cliente")
    elif opcion == "5":
        print("salimos")
        exit()

