from . import db

def cursos(campus):
    return db.distinct("curso", { "campus": campus })