from dataclasses import dataclass
from src.usuario.domain.usuario import Usuario
from src.geral.infrastructure.repository_interface import RepositoryInterface
from typing import Optional


@dataclass
class CreateUsuarioRequest:
    login: str
    email: str
    senha: str


@dataclass
class CreateUsuarioResponse:
    id: str
    login: str
    email: str
    message: str


class CreateUsuarioUseCase:
    def __init__(self, usuario_repository: RepositoryInterface):
        self.usuario_repository = usuario_repository

    def execute(self, request: CreateUsuarioRequest) -> CreateUsuarioResponse:
        """
        Executa o caso de uso de criação de usuário
        
        Args:
            request: Dados do usuário a ser criado
            
        Returns:
            Resposta com os dados do usuário criado
            
        Raises:
            ValueError: Se houver erro na validação ou se login/email já existir
        """
        try:
            # Cria o usuário (validações são feitas no construtor)
            usuario = Usuario(
                id=None,  # ID será gerado pelo repositório
                login=request.login,
                email=request.email,
                senha=request.senha
            )
            
            # Salva o usuário (repositório verifica duplicatas)
            usuario_salvo = self.usuario_repository.save(usuario)
            
            return CreateUsuarioResponse(
                id=usuario_salvo.id,
                login=usuario_salvo.login,
                email=usuario_salvo.email,
                message="Usuário criado com sucesso"
            )
            
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise ValueError(f"Erro interno ao criar usuário: {str(e)}")


if __name__ == "__main__":
    from src.usuario.infrastructure.usuario_repository import UsuarioRepository
    
    # Teste do use case
    repo = UsuarioRepository()
    use_case = CreateUsuarioUseCase(repo)
    
    request = CreateUsuarioRequest(
        login="teste_use_case",
        email="teste_use_case@email.com",
        senha="senha123"
    )
    
    try:
        response = use_case.execute(request)
        print(f"Usuário criado: {response}")
    except ValueError as e:
        print(f"Erro: {e}")