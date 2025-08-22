from flask import Blueprint, request, jsonify
from src.curso.application.use_cases.create.create_curso_use_case import (
    CreateCursoUseCase,
    CreateCursoRequest,
)
from src.curso.infrastructure.curso_repository import CursoRepository

cursos_bp = Blueprint("cursos", __name__)
curso_repository = CursoRepository()
create_curso_use_case = CreateCursoUseCase(curso_repository)


@cursos_bp.route("/api/cursos", methods=["POST"])
def create_curso():
    data = request.get_json()
    curso_request = CreateCursoRequest(
        nome=data["nome"], descricao=data["descricao"], horas=data["horas"]
    )
    try:
        curso_response = create_curso_use_case.execute(curso_request)
        return jsonify(curso_response), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
