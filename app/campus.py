from .db import get_estudantes_collection

def get_cursos(campus):
    collection = get_estudantes_collection()

    return collection.distinct("curso", { "campus": campus })

def count_alunos(campus, start_date, end_date):
    collection = get_estudantes_collection()

    return collection.count_documents({ "campus": campus, "data_inicio": { "$gte": start_date, "$lte": end_date } })

def get_aluno(campus, ra):
    collection = get_estudantes_collection()

    aluno = collection.find_one({ "campus": campus, "ra": ra })

    return aluno