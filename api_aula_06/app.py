from flask import request, jsonify
from app_config import app, db
from models.aluno import Aluno

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict())

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        curso=data['curso'],
        nota=data['nota']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201

@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    data = request.get_json()
    aluno = Aluno.query.get_or_404(id)
    aluno.nome = data['nome']
    aluno.idade = data['idade']
    aluno.curso = data['curso']
    aluno.nota = data['nota']
    db.session.commit()
    return jsonify(aluno.to_dict())

@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)