from . import db

schema = {
    'type': 'object',
    'properties': {
        'nome': { 'type': 'string' },
        'idade_ate_31_12_2016': { 'type': 'number' },
        'ra': { 'type': 'number' },
        'campus': { 'type': 'string' },
        'municipio': { 'type': 'string' },
        'curso': { 'type': 'string' },
        'modalidade': { 'type': 'string' },
        'nivel_do_curso': { 'type': 'string' },
        'data_inicio': { 'type': 'string', 'format': 'date-time' }
    },
    'required': [
        "nome",
        "idade_ate_31_12_2016",
        "ra",
        "campus",
        "municipio",
        "curso",
        "modalidade",
        "nivel_do_curso",
        "data_inicio"
    ]
}

def insert(aluno):
    return db.insert(aluno)

def delete(aluno):
    db.delete({ '_id': aluno['_id'] })

def get_many(filter):
    return db.get_many(filter)

def get_one(filter):
    return db.get_one(filter)

def count(filter):
    return db.count(filter)