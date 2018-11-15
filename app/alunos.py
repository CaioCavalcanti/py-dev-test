from . import db

def delete(aluno):
    db.delete({ "_id": aluno["_id"] })

def get_many(filter):
    return db.get_many(filter)

def get_one(filter):
    return db.get_one(filter)

def count(filter):
    return db.count(filter)