from .db import get_estudantes_collection

def get_cursos(campus):
    collection = get_estudantes_collection()

    return collection.distinct("curso", { "campus": campus })