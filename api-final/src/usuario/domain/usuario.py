import hashlib
import re
from typing import Optional


class Usuario:
    def __init__(self, id: Optional[str], login: str, email: str, senha: str, senha_hash: Optional[str] = None):
        """
        Cria um novo usuário.
        
        Args:
            id: ID único do usuário (None para novos usuários)
            login: Login único do usuário
            email: Email único do usuário
            senha: Senha em texto plano (será criptografada)
            senha_hash: Hash da senha (usado ao carregar do banco)
        """
        try:
            self.validar_login(login)
            self.validar_email(email)
            if senha_hash is None:
                self.validar_senha(senha)
            
            self.id = id
            self.login = login
            self.email = email
            
            # Se já temos o hash, usa ele; senão, criptografa a senha
            if senha_hash:
                self.senha_hash = senha_hash
            else:
                self.senha_hash = self._criptografar_senha(senha)
                
        except ValueError as e:
            raise ValueError(f"Erro ao criar usuário: {e}")

    def validar_login(self, login: str):
        """Valida o login do usuário"""
        if not login:
            raise ValueError("Login não pode ser vazio.")
        if len(login) < 3:
            raise ValueError("Login deve ter pelo menos 3 caracteres.")
        if len(login) > 50:
            raise ValueError("Login deve ter no máximo 50 caracteres.")
        if not re.match(r'^[a-zA-Z0-9_]+$', login):
            raise ValueError("Login deve conter apenas letras, números e underscore.")

    def validar_email(self, email: str):
        """Valida o email do usuário"""
        if not email:
            raise ValueError("Email não pode ser vazio.")
        

    def validar_senha(self, senha: str):
        """Valida a senha do usuário"""
        if not senha:
            raise ValueError("Senha não pode ser vazia.")
        if len(senha) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres.")
        if len(senha) > 100:
            raise ValueError("Senha deve ter no máximo 100 caracteres.")

    def _criptografar_senha(self, senha: str) -> str:
        """Criptografa a senha usando SHA-256 com salt"""
        salt = "sollaris_salt_2024"  # Em produção, use um salt único por usuário
        senha_com_salt = senha + salt
        return hashlib.sha256(senha_com_salt.encode()).hexdigest()

    def verificar_senha(self, senha: str) -> bool:
        """Verifica se a senha fornecida está correta"""
        senha_hash = self._criptografar_senha(senha)
        return senha_hash == self.senha_hash

    def to_dict(self) -> dict:
        """Converte o usuário para dicionário (sem a senha)"""
        return {
            "id": self.id,
            "login": self.login,
            "email": self.email
        }

    def __repr__(self):
        return f"Usuario(id={self.id}, login={self.login}, email={self.email})"


if __name__ == "__main__":
    # Teste da classe
    usuario = Usuario(None, "joao123", "joao@email.com", "senha123")
    print(usuario)
    print(f"Senha correta: {usuario.verificar_senha('senha123')}")
    print(f"Senha incorreta: {usuario.verificar_senha('senha456')}")