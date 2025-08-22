from src.geral.infrastructure.repository_interface import RepositoryInterface
from src.usuario.domain.usuario import Usuario
import json
import os
from typing import Optional, List
import uuid


class UsuarioRepository(RepositoryInterface):
    def __init__(self, arquivo_json: str = "usuarios.json"):
        self.arquivo_json = arquivo_json
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        """Cria o arquivo JSON se não existir"""
        if not os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def _carregar_usuarios(self) -> List[dict]:
        """Carrega todos os usuários do arquivo JSON"""
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _salvar_usuarios(self, usuarios: List[dict]):
        """Salva a lista de usuários no arquivo JSON"""
        with open(self.arquivo_json, "w", encoding="utf-8") as file:
            json.dump(usuarios, file, ensure_ascii=False, indent=4)

    def save(self, usuario: Usuario) -> Usuario:
        """Salva um novo usuário"""
        usuarios = self._carregar_usuarios()
        
        # Gera um ID único se não tiver
        if not usuario.id:
            usuario.id = str(uuid.uuid4())
        
        # Verifica se login já existe
        if self.existe_login(usuario.login):
            raise ValueError(f"Login '{usuario.login}' já está em uso")
        
        # Verifica se email já existe
        if self.existe_email(usuario.email):
            raise ValueError(f"Email '{usuario.email}' já está em uso")
        
        # Adiciona o usuário
        usuarios.append({
            "id": usuario.id,
            "login": usuario.login,
            "email": usuario.email,
            "senha_hash": usuario.senha_hash
        })
        
        self._salvar_usuarios(usuarios)
        return usuario

    def buscar_por_login(self, login: str) -> Optional[Usuario]:
        """Busca um usuário pelo login"""
        usuarios = self._carregar_usuarios()
        for usuario_data in usuarios:
            if usuario_data["login"] == login:
                return Usuario(
                    id=usuario_data["id"],
                    login=usuario_data["login"],
                    email=usuario_data["email"],
                    senha="",  # Não precisamos da senha original
                    senha_hash=usuario_data["senha_hash"]
                )
        return None

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca um usuário pelo email"""
        usuarios = self._carregar_usuarios()
        for usuario_data in usuarios:
            if usuario_data["email"] == email:
                return Usuario(
                    id=usuario_data["id"],
                    login=usuario_data["login"],
                    email=usuario_data["email"],
                    senha="",  # Não precisamos da senha original
                    senha_hash=usuario_data["senha_hash"]
                )
        return None

    def buscar_por_id(self, id: str) -> Optional[Usuario]:
        """Busca um usuário pelo ID"""
        usuarios = self._carregar_usuarios()
        for usuario_data in usuarios:
            if usuario_data["id"] == id:
                return Usuario(
                    id=usuario_data["id"],
                    login=usuario_data["login"],
                    email=usuario_data["email"],
                    senha="",  # Não precisamos da senha original
                    senha_hash=usuario_data["senha_hash"]
                )
        return None

    def existe_login(self, login: str) -> bool:
        """Verifica se um login já existe"""
        return self.buscar_por_login(login) is not None

    def existe_email(self, email: str) -> bool:
        """Verifica se um email já existe"""
        return self.buscar_por_email(email) is not None

    def listar_todos(self) -> List[Usuario]:
        """Lista todos os usuários"""
        usuarios = self._carregar_usuarios()
        return [
            Usuario(
                id=usuario_data["id"],
                login=usuario_data["login"],
                email=usuario_data["email"],
                senha="",
                senha_hash=usuario_data["senha_hash"]
            )
            for usuario_data in usuarios
        ]


if __name__ == "__main__":
    # Teste do repositório
    repo = UsuarioRepository()
    
    # Criar usuário de teste
    usuario = Usuario(None, "teste123", "teste@email.com", "senha123")
    usuario_salvo = repo.save(usuario)
    print(f"Usuário salvo: {usuario_salvo}")
    
    # Buscar usuário
    usuario_encontrado = repo.buscar_por_login("teste123")
    print(f"Usuário encontrado: {usuario_encontrado}")
    
    # Verificar senha
    if usuario_encontrado:
        print(f"Senha correta: {usuario_encontrado.verificar_senha('senha123')}")