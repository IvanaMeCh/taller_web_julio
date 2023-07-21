#importamos de la libreria flask, la clase Flask para poder construir la aplicacion
from flask import Flask, render_template
#importamos requests para poder hacer las consultas a la api
import requests
#Inicializar la aplicacion de Flask creando una variable y diciendole que va tener la forma de la clase Flask
app=Flask(__name__)

#Creamos nuestra ruta para que nuestra aplicacion pueda ser accedida desde el navegador, la barra / indica que es la pagina principal
@app.route('/')

#esta es la funcion que se va ejecutar cuando ingresemos a la ruta principal
def pagina_principal():

    return "hola mundo! desde el taller web"

#creamos nuestra nueva ruta llamada ejemplo
@app.route('/ejemplo')
def ejemplo():
    #con render_template hacemos que la ruta se conecte con la vista que creamos en templates
    return render_template('ejemplo.html')

@app.route('/enviar_datos')

def enviar_datos():
    nombre = "Jere"
    apellido = "Larrosa"
    #vamos a enviar datos desde el back (app.py) al front (enviar_datos.html) 
    return render_template('enviar_datos.html',nombre=nombre,apellido=apellido)

@app.route('/personaje')

def personaje():
    #esta url (api de rick and morty) es a la que hacemos el pedido (podemos ir a la url a ver que tipo de datos nos devuelve)
    api_url = 'https://rickandmortyapi.com/api/character/198'
    
    #con requests.get hacemos el pedido a la api y con .json() convertimos la respuesta a un diccionario
    respuesta_api = requests.get(api_url).json()
    
    # Sabiendo que la respuesta es un diccionario creamos variables para almacenar los datos del diccionario que queremos pasar a personaje.html
    nombre= respuesta_api['name']
    estado = respuesta_api['status']
    url_imagen = respuesta_api['image']
    #pasamos como parametro las variables que creamos para usar con jinja en nuestra vista personaje.html
    return render_template("personaje.html",nombre=nombre, estado=estado,url_imagen=url_imagen)

@app.route('/personajes')
def personajes():
    #vamos a esta url donde estan todos los personajes y vemos que tipo de datos nos esta devolviendo para saber como manejar
    url = 'https://rickandmortyapi.com/api/character'
    
    #con requests.get hacemos el pedido a la api y con .json() convertimos la respuesta a un diccionario
    respuesta_api = requests.get(url).json()
    
    # Si vemos la respuesta de la api vemos que la respuesta es un diccionario y que dentro de este diccionario hay una lista de personajes almacenada con la clave "results", entonces creamos una variable para almacenar esta lista de personajes
    lista_de_personajes = respuesta_api['results']

    # Enviamos la lista de personas a la vista para poder mostrarla con jinja por medio de render template
    return render_template("lista_de_personajes.html",lista_de_personajes=lista_de_personajes)



# va al fondo porque sirve para darle funcionalidad al boton de play o compilador de arriba 
if __name__ == '__main__': 
    app.run (debug=True)