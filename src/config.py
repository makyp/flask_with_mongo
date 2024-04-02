#certifi: valida que la conexión que recibimos de mongoDB sea segura y  valida
#pymongo[srv]: Manejo del servicicio DNS por parte de pymongo 
from pymongo import MongoClient
import certifi
MONGO='mongodb+srv://makyp:Pacho040321@cluster0.yjkbst6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

#Crear el certificado de seguridad
certificado = certifi.where()

#Funcion que nos permitira conectarno con la base de datos
def Conexion():
    try:
        client = MongoClient(MONGO, tlsCAFile=certificado)
        #Crea la base de datos llamada bd_personas
        bd = client["bd_personas"]
        print('Conexión Exitosa')
    except ConnectionError:
        print('Eror de conexión')
    return bd

Conexion();#Inicializarla