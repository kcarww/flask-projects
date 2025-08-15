# main.py - Versão organizada com camadas
from flask import Flask
from src.aluno.infrastructure.routes.aluno_routes import aluno_bp
from src.shared.config.app_config import AppConfig
from src.shared.middleware.error_handler import register_error_handlers
import os

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config.from_object(AppConfig)
    
    # Registrar blueprints (rotas)
    app.register_blueprint(aluno_bp, url_prefix='/api')
    
    # Registrar middleware de tratamento de erros
    register_error_handlers(app)
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'OK', 'message': 'API funcionando'}, 200
    
    return app

def main():
    """Função principal para inicializar a aplicação"""
    app = create_app()
    
    # Configurações do servidor
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    
    print(f"🚀 Iniciando servidor em http://{host}:{port}")
    print(f"🔧 Debug mode: {debug}")
    
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    main()
