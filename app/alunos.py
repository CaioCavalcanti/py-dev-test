from .db import get_estudantes_collection

def delete_aluno(aluno):
    collection = get_estudantes_collection()

    collection.delete_one({ "_id": aluno["_id"] })