class Aluno:
    def __init__(self, matricula: str, nome: str, idade: int, curso: str):
        try:
            self.validar_nome(nome)
            self.validar_idade(idade)
            self.validar_curso(curso)

            self.matricula = matricula
            self.nome = nome
            self.idade = idade
            self.curso = curso
        except ValueError as e:
            raise ValueError(f"Erro ao criar aluno: {e}")

    def validar_nome(self, nome: str):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if len(nome) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")

    def validar_idade(self, idade: int):
        if not isinstance(idade, int):
            raise ValueError("Idade deve ser um número inteiro.")

        if idade < 0:
            raise ValueError("Idade não pode ser negativa.")

    def validar_curso(self, curso: str):
        if not curso:
            raise ValueError("Curso não pode ser vazio.")

    def __repr__(self):
        return f"Aluno(matricula={self.matricula}, nome={self.nome}, idade={self.idade}, curso={self.curso})"


if __name__ == "__main__":
    print(Aluno("000001", "João da Silva", 20, "Engenharia"))
