from datetime import datetime
from flask import Flask, request, jsonify, make_response
from uuid import uuid4

# Local
from . import campus
from . import alunos

app = Flask(__name__)

# TODO: load env variables

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/modalidade/<modalidade_id>/alunos', methods=['GET'])
def retornar_alunos_por_modalidade(modalidade_id):
    # params modalidade, data de inicio e data de fim
    # retorno lista de todos os itens no período selecionado
    # ordenado de forma decrescente
    # validar modalidade

    return jsonify(modalidade_id)

@app.route('/api/campus/<campus_id>/cursos', methods=['GET'])
def retornar_cursos_por_campus(campus_id):
    cursos = campus.get_cursos(campus_id)
    cursos.sort()

    return jsonify(cursos)

@app.route('/api/campus/<campus_id>/alunos', methods=['GET'])
def retornar_alunos_por_campus(campus_id):
    start_date_str = request.args.get('de')
    end_date_str = request.args.get('ate')

    if(start_date_str is None or end_date_str is None):
        return bad_request("Período não informado")
    
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y')
    end_date = datetime.strptime(end_date_str, '%d/%m/%Y')

    if end_date < start_date:
        return bad_request("O período selecionado não é válido")

    total_alunos = campus.count_alunos(campus_id, start_date, end_date)

    return jsonify(total_alunos)

@app.route('/api/alunos', methods=['POST'])
def cadastrar_aluno():
    # Paylod: nome, idade_ate_31_12_2016, ra, campus,municipio, curso
    # modalidade, nivel_do_curso, data_inicio
    # retorno 201 com o mesmo payload
    # validar duplicados
    print(request.get_json())

    return jsonify(str(request.data)), 201

@app.route('/api/campus/<campus_id>/alunos/<ra>', methods=['DELETE'])
def remover_aluno(campus_id, ra):
    aluno = campus.get_aluno(campus_id, int(ra))

    if aluno is None:
        return not_found("Não foi possível encontrar o aluno com RA '%s' no campus '%s'" % (ra, campus_id))

    alunos.delete_aluno(aluno)

    return make_response()

@app.errorhandler(500)
def tratar_internal_server_error(e):
    return internal_server_error(e)

def internal_server_error(error):
    erro_id = uuid4()
    # TODO: logar erro usando id como referencia

    res = dict()
    message = "Ocorreu um erro ao processar sua request" if app.debug else str(error)

    res['message'] = message
    res['id'] = str(erro_id)

    return jsonify(res), 500


def bad_request(message):
    res = dict()

    res['message'] = message

    return jsonify(res), 400

def not_found(message):
    res = dict()

    res['message'] = message

    return jsonify(res), 404