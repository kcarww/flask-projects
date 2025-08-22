from dataclasses import dataclass
from src.usuario.infrastructure.usuario_repository import UsuarioRepository
from src.auth.jwt_service import JWTService
from typing import Optional


@dataclass
class AuthenticateUsuarioRequest:
    login: str
    senha: str


@dataclass
class AuthenticateUsuarioResponse:
    token: str
    user_id: str
    login: str
    email: str
    message: str


class AuthenticateUsuarioUseCase:
    def __init__(self, usuario_repository: UsuarioRepository, jwt_service: JWTService):
        self.usuario_repository = usuario_repository
        self.jwt_service = jwt_service

    def execute(self, request: AuthenticateUsuarioRequest) -> AuthenticateUsuarioResponse:
        """
        Executa o caso de uso de autenticação de usuário
        
        Args:
            request: Credenciais do usuário
            
        Returns:
            Resposta com token JWT e dados do usuário
            
        Raises:
            ValueError: Se as credenciais forem inválidas
        """
        try:
            # Busca o usuário pelo login
            usuario = self.usuario_repository.buscar_por_login(request.login)
            
            if not usuario:
                raise ValueError("Credenciais inválidas")
            
            # Verifica a senha
            if not usuario.verificar_senha(request.senha):
                raise ValueError("Credenciais inválidas")
            
            # Gera o token JWT
            token = self.jwt_service.gerar_token(
                usuario_id=usuario.id,
                login=usuario.login,
                email=usuario.email
            )
            
            return AuthenticateUsuarioResponse(
                token=token,
                user_id=usuario.id,
                login=usuario.login,
                email=usuario.email,
                message="Login realizado com sucesso"
            )
            
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise ValueError(f"Erro interno na autenticação: {str(e)}")


if __name__ == "__main__":
    # Teste do use case
    repo = UsuarioRepository()
    jwt_service = JWTService()
    use_case = AuthenticateUsuarioUseCase(repo, jwt_service)
    
    # Primeiro, criar um usuário para testar
    from src.usuario.domain.usuario import Usuario
    usuario_teste = Usuario(None, "teste_auth", "teste_auth@email.com", "senha123")
    repo.save(usuario_teste)
    
    # Testar autenticação
    request = AuthenticateUsuarioRequest(
        login="teste_auth",
        senha="senha123"
    )
    
    try:
        response = use_case.execute(request)
        print(f"Autenticação bem-sucedida: {response}")
    except ValueError as e:
        print(f"Erro na autenticação: {e}")