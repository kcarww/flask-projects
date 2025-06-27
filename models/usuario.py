class Usuario:
    def __init__(self, id: str, nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"
    
