from src.domain.funcionario import Funcionario

class Consultor(Funcionario):
    def __init__(self, matricula, nome, loja, senha):
        super().__init__(matricula, nome, loja, senha)

    def __str__(self):
        return f"Consultor(matricula={self.matricula}, nome='{self.nome}', loja='{self.loja}')"