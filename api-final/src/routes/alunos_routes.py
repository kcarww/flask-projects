from flask import Blueprint, request, jsonify
from src.aluno.application.use_cases.create.create_aluno_use_case import (
    CreateAlunoUseCase,
    CreateAlunoRequest,
)
from src.aluno.infrastructure.aluno_repository import AlunoRepository
from src.auth.jwt_service import token_required

aluno_bp = Blueprint("alunos", __name__)
aluno_repository = AlunoRepository()
create_aluno_use_case = CreateAlunoUseCase(aluno_repository)


@aluno_bp.route("/api/alunos", methods=["POST"])
@token_required
def cadastrar_aluno():
    dados_aluno = request.json
    create_request = CreateAlunoRequest(
        nome=dados_aluno["nome"], idade=dados_aluno["idade"], curso=dados_aluno["curso"]
    )
    novo_aluno = create_aluno_use_case.execute(create_request)
    return jsonify(novo_aluno), 201
