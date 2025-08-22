from flask import Flask
from src.routes.alunos_routes import aluno_bp
from src.routes.cursos_routes import cursos_bp
from src.routes.auth_routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(aluno_bp)
    app.register_blueprint(cursos_bp)
    app.register_blueprint(auth_bp)
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
