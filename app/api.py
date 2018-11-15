from flask import Flask, request, jsonify, make_response
from uuid import uuid4

# Local
from . import campus

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
    # param campus, data inicio e data fim
    # retornar número de alunos no campus no periodo selecionado
    # tratar campus não encontrado
    # tratar período inválido

    # O enunciado não deixa explícito se deveria ser uma Restful API ou não
    # então parti do princípio que /count é válido nesse contexto. Mas
    # para ser restful este endpoint deveria tratar apenas da lista de alunos,
    # onde o total pode ser retornado em um header (ex: X-Total-Count).

    return jsonify(campus_id)

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
    # params campus e RA
    # retorno 200

    return make_response()

@app.errorhandler(500)
def tratar_internal_server_error(e):
    erro_id = uuid4()
    # TODO: logar erro usando id como referencia

    res = dict()
    message = "Ocorreu um erro ao processar sua request" if app.debug else str(e)

    res['message'] = message
    res['id'] = str(erro_id)

    return jsonify(res), 500