class Funcionario:
    def __init__(self, matricula, nome, loja, senha):
        self.matricula = matricula
        self.nome = nome
        self.loja = loja
        self.senha = senha

    def __str__(self):
        return f"Funcionario(matricula={self.matricula}, nome='{self.nome}', loja='{self.loja}')"