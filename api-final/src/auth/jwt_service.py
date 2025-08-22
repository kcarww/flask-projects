import jwt
import datetime
from typing import Dict, Optional
from functools import wraps
from flask import request, jsonify, current_app


class JWTService:
    def __init__(self, secret_key: str = "sollaris_jwt_secret_2024", expiration_hours: int = 24):
        """
        Inicializa o serviço JWT
        
        Args:
            secret_key: Chave secreta para assinar os tokens
            expiration_hours: Tempo de expiração do token em horas
        """
        self.secret_key = secret_key
        self.expiration_hours = expiration_hours
        self.algorithm = "HS256"

    def gerar_token(self, usuario_id: str, login: str, email: str) -> str:
        """
        Gera um token JWT para o usuário
        
        Args:
            usuario_id: ID único do usuário
            login: Login do usuário
            email: Email do usuário
            
        Returns:
            Token JWT como string
        """
        payload = {
            'user_id': usuario_id,
            'login': login,
            'email': email,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=self.expiration_hours)
        }
        
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def validar_token(self, token: str) -> Optional[Dict]:
        """
        Valida um token JWT
        
        Args:
            token: Token JWT para validar
            
        Returns:
            Payload do token se válido, None se inválido
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def extrair_token_do_header(self, authorization_header: str) -> Optional[str]:
        """
        Extrai o token do header Authorization
        
        Args:
            authorization_header: Header Authorization (formato: "Bearer <token>")
            
        Returns:
            Token JWT ou None se inválido
        """
        if not authorization_header:
            return None
        
        parts = authorization_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return None
        
        return parts[1]


# Instância global do serviço JWT
jwt_service = JWTService()


def token_required(f):
    """
    Decorator para proteger rotas que requerem autenticação
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            token = jwt_service.extrair_token_do_header(auth_header)
        
        if not token:
            return jsonify({
                'error': 'Token de acesso é obrigatório',
                'message': 'Forneça um token válido no header Authorization: Bearer <token>'
            }), 401
        
        payload = jwt_service.validar_token(token)
        if not payload:
            return jsonify({
                'error': 'Token inválido ou expirado',
                'message': 'Faça login novamente para obter um novo token'
            }), 401
        
        # Adiciona os dados do usuário ao contexto da requisição
        request.current_user = {
            'user_id': payload['user_id'],
            'login': payload['login'],
            'email': payload['email']
        }
        
        return f(*args, **kwargs)
    
    return decorated


if __name__ == "__main__":
    # Teste do serviço JWT
    service = JWTService()
    
    # Gerar token
    token = service.gerar_token("123", "joao", "joao@email.com")
    print(f"Token gerado: {token}")
    
    # Validar token
    payload = service.validar_token(token)
    print(f"Payload: {payload}")
    
    # Testar header
    header = f"Bearer {token}"
    token_extraido = service.extrair_token_do_header(header)
    print(f"Token extraído: {token_extraido}")