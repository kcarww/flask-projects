from src.geral.infrastructure.repository_interface import RepositoryInterface
from src.aluno.domain.aluno import Aluno
import json


class AlunoRepository(RepositoryInterface):

    def carregar_alunos_json(self):
        with open("alunos.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, aluno: Aluno):
        alunos = self.carregar_alunos_json()
        alunos.append(
            {
                "matricula": aluno.matricula,
                "nome": aluno.nome,
                "idade": aluno.idade,
                "curso": aluno.curso,
            }
        )
        with open("alunos.json", "w", encoding="utf-8") as file:
            json.dump(alunos, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    aluno_novo = Aluno("20231008", "Joana Silva", 20, "Engenharia")
    aluno_repository = AlunoRepository()
    aluno_repository.save(aluno_novo)
    print(f"Aluno {aluno_novo.nome} salvo com sucesso!")
