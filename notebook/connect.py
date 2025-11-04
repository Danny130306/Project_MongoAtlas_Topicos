from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    db_atlas = client[DB_NAME_ATLAS]
    print("Conexión exitosa a MongoDB Atlas")
    colecciones = db_atlas.list_collection_names()
    print('Conectando a la base de datos:', DB_NAME_ATLAS)
    print("Colecciones en la base de datos:", colecciones)
except :
    print(f" Error al conectar a MongoDB Atlas")
