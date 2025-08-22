from flask import Blueprint, request, jsonify
from src.usuario.application.use_cases.create.create_usuario_use_case import (
    CreateUsuarioUseCase, CreateUsuarioRequest
)
from src.usuario.application.use_cases.authenticate.authenticate_usuario_use_case import (
    AuthenticateUsuarioUseCase, AuthenticateUsuarioRequest
)
from src.usuario.infrastructure.usuario_repository import UsuarioRepository
from src.auth.jwt_service import JWTService

auth_bp = Blueprint("auth", __name__)
_usuario_repo = UsuarioRepository()
_jwt_service = JWTService()
_create_usuario_uc = CreateUsuarioUseCase(_usuario_repo)
_authenticate_usuario_uc = AuthenticateUsuarioUseCase(_usuario_repo, _jwt_service)


@auth_bp.route("/api/auth/cadastrar", methods=["POST"])
def cadastrar_usuario():
    data = request.get_json() or {}
    try:
        req = CreateUsuarioRequest(
            login=data.get("login", "").strip(),
            email=data.get("email", "").strip(),
            senha=data.get("senha", "")
        )
        res = _create_usuario_uc.execute(req)
        # Gera token imediatamente após cadastro
        token = _jwt_service.gerar_token(
            usuario_id=res.id,
            login=res.login,
            email=res.email
        )
        return jsonify({
            "message": res.message,
            "user": {"id": res.id, "login": res.login, "email": res.email},
            "token": token,
            "type": "Bearer"
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Erro interno: {e}"}), 500


@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    try:
        req = AuthenticateUsuarioRequest(
            login=data.get("login", "").strip(),
            senha=data.get("senha", "")
        )
        res = _authenticate_usuario_uc.execute(req)
        return jsonify({
            "message": res.message,
            "user": {"id": res.user_id, "login": res.login, "email": res.email},
            "token": res.token,
            "type": "Bearer"
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        return jsonify({"error": f"Erro interno: {e}"}), 500