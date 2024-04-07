##Se recomienda nombrar las clases con la primera en mayúscula
class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        ##El self lo que muestra es referise a los atributos ej self.nombre, los cuales se inicializan con los parametros es decir = nombre, este metodo constructor no necesita retorno.
    
    #Metodo para solicitar todos los atributos de la persona actual y los devuelve en un formato tipo diccionario, es decir formatea los datos a ingresar en un documeto de clave de valor para que lo reconozca la base de datos.   
    def formato_doc(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
        }
        
        
        
    