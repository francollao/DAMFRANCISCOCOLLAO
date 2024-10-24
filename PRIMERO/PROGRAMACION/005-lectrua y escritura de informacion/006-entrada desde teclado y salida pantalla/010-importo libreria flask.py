from flask import Flask #importamos libreria que permite crear miniservidor web
aplicacion = Flask(__name__) #creo servidor web

mensaje = '{"resultado":"ok"}'

print(mensaje)