class Curso:
    def __init__(self, id: int, nome: str, descricao: str, horas: int):
        try:
            self.validar_nome(nome)
            self.validar_horas(horas)
            self.validar_descricao(descricao)

            self.id = id
            self.nome = nome
            self.descricao = descricao
            self.horas = horas
        except (ValueError, TypeError) as e:
            raise e

    def __repr__(self):
        return f"Curso(id={self.id}, nome='{self.nome}', descricao='{self.descricao}', horas={self.horas})"

    def validar_nome(self, nome: str) -> bool:
        if len(nome) < 3:
            raise ValueError("O nome do curso deve ter pelo menos 3 caracteres.")

        if not nome:
            raise ValueError("O nome do curso não pode ser vazio.")

        if not isinstance(nome, str):
            raise TypeError("O nome do curso deve ser uma string.")

    def validar_horas(self, horas: int) -> bool:
        if horas <= 0:
            raise ValueError("O número de horas do curso deve ser maior que zero.")

        if not isinstance(horas, int):
            raise TypeError("O número de horas do curso deve ser um inteiro.")

    def validar_descricao(self, descricao: str) -> bool:
        if len(descricao) < 10:
            raise ValueError("A descrição do curso deve ter pelo menos 10 caracteres.")
