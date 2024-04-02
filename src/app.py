from flask import Flask, render_template, request, redirect, url_for
from config import *
from persona import Persona


##Crear instancia de conexión a la base de datos y debe ir antes de crear la instancia de la aplicación
con_bd = Conexion()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/guardar_personas', methods=['POST'])
def agregarPersona():
    colection_personas = con_bd['Personas']##Estamos creando una colección llamada personas en la base de datos
    nombre = request.form['nombre']##Obtengo los datos del index
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    if nombre and apellido and telefono:#Valido que no este vacio
        object_persona =Persona(nombre, apellido, telefono)#Creo un objeto persona a partir de la clase persona que recibe los parametros
        colection_personas.insert_one(object_persona.formato_doc())#Inserto ese objeto a la base de datos a partir de la colección definida anteriormente llamada personas dandole el formato del documento
        return redirect(url_for('index'))
    else: 
        return "Error"

if __name__ == '__main__':
    
    
    app.run(debug=True, port=5555)