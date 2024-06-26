from flask import Flask, render_template, request, redirect, url_for
from config import *
from persona import Persona


##Crear instancia de conexión a la base de datos y debe ir antes de crear la instancia de la aplicación
con_bd = Conexion()

app = Flask(__name__)

@app.route('/')
def index():
    colection_personas = con_bd['Personas']
    #. find() Permite consultar la colección completa y lo almacena en un objeto
    PersonasRegistradas = colection_personas.find()
    
    return render_template("index.html", personas = PersonasRegistradas)

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
# ##Ruta para eliminar un dato   
# @app.route('/eliminar_persona/<string:nombre_persona>')
# def eliminar(nombre_persona):
#     colection_personas = con_bd['Personas']
#     colection_personas.delete_one({'nombre': nombre_persona})
#     return redirect(url_for('index'))
@app.route('/eliminar_persona', methods=['GET', 'POST'])
def eliminar_persona():
    if request.method == 'POST':
        nombre_persona = request.form['nombre_persona']
        coleccion_personas = con_bd['Personas']
        persona = coleccion_personas.find_one({'nombre': nombre_persona})
        if persona:
            coleccion_personas.delete_one({'nombre': nombre_persona})
            return redirect(url_for('index'))
        else:
            return "La persona especificada no existe."
    else:
        coleccion_personas = con_bd['Personas']
        personas = coleccion_personas.find() 
        return render_template('eliminar.html', personas=personas)


@app.route("/editar_personas/<string:nombre_persona>", methods=['GET', 'POST'])
def editar(nombre_persona):
    colection_personas = con_bd['Personas']
    personas = colection_personas.find()  # Obtener todas las personas
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        
        if nombre and apellido and telefono:
            colection_personas.update_one({'nombre': nombre_persona}, {'$set': {'nombre': nombre, 'apellido': apellido, 'telefono': telefono}})
            return redirect(url_for('index'))
        else:
            return "Error: Todos los campos son obligatorios"
    else:
        return render_template('editar.html', personas=personas)  # Pasar todas las personas a la plantilla



  
if __name__ == '__main__':
    app.run(debug=True, port=5555)