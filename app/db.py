import os
from pymongo import MongoClient

# TODO: db as singleton class to share collection/db single connection

def connect_db():
    host = os.environ["MONGODB_HOST"]
    port = int(os.environ["MONGODB_PORT"])

    connection = MongoClient(host, port)
    db = connection.caioCavalcanti

    return db

def get_collection():
    db = connect_db()

    return db.estudantes

def delete(filter):
    collection = get_collection()

    collection.delete_one(filter)

def get_many(filter):
    collection = get_collection()

    return collection.find(filter, { '_id': False})

def get_one(filter):
    collection = get_collection()

    return collection.find_one(filter)

def count(filter):
    collection = get_collection()

    return collection.count_documents(filter)

def distinct(field, filter):
    collection = get_collection()

    return collection.distinct(field, filter)