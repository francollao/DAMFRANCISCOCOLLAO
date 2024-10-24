from flask import Flask #importamos libreria que permite crear miniservidor web
aplicacion = Flask(__name__) #creo servidor web

@aplicacion.route('/')      #creo escuchador para que este pendiente cuando alguien entre en la raiz
def inicio():   #defino funcion
    contenido = {"resultado":"ok"}  #preparo contenido
    return contenido   #lanzo el contenido al navegador web

aplicacion.run(debug=True)  #arranco el servidor 

