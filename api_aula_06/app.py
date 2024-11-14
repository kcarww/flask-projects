from flask import request, jsonify
from app_config import app, db
from models.aluno import Aluno
from models.user import User
from hash_password_handler import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/alunos', methods=['GET'])
@jwt_required()
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route('/alunos/<int:id>', methods=['GET'])
@jwt_required()
def obter_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict())

@app.route('/alunos', methods=['POST'])
@jwt_required()
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
@jwt_required()
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
@jwt_required()
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return '', 204

@app.route('/user', methods=['GET'])
def listar_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/user/<int:id>', methods=['GET'])
def obter_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/user', methods=['POST'])
def criar_user():
    data = request.get_json()
    hashed_password = create_password_hash(data['password'])
    novo_user = User(
        username=data['username'],
        password=hashed_password
    )
    db.session.add(novo_user)
    db.session.commit()
    return jsonify(novo_user.to_dict()), 201

@app.route('/user/<int:id>', methods=['PUT'])
def atualizar_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.username = data['username']
    user.password = create_password_hash(data['password'])

    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/user/<int:id>', methods=['DELETE'])
def deletar_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and verify_password_hash(str(user.password), data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"Erro": "Falha na autenticação"}), 401

if __name__ == '__main__':
    app.run(debug=True)