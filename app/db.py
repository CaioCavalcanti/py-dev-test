import os
from pymongo import MongoClient

CONNECTION = MongoClient()

def connect_db():
    host = os.environ["MONGODB_HOST"]
    port = int(os.environ["MONGODB_PORT"])

    connection = MongoClient(host, port)
    db = connection.caioCavalcanti

    return db

def get_estudantes_collection():
    db = connect_db()

    return db.estudantes