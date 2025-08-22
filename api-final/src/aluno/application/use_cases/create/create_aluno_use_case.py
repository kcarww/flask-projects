from dataclasses import dataclass
from src.aluno.domain.aluno import Aluno
from src.geral.infrastructure.repository_interface import RepositoryInterface
from src.aluno.infrastructure.aluno_repository import AlunoRepository
import random


@dataclass
class CreateAlunoResponse:
    matricula: str
    nome: str
    idade: int
    curso: str


@dataclass
class CreateAlunoRequest:
    nome: str
    idade: int
    curso: str


class CreateAlunoUseCase:
    def __init__(self, aluno_repository: RepositoryInterface):
        self.aluno_repository = aluno_repository

    def execute(self, request: CreateAlunoRequest) -> CreateAlunoResponse:
        try:
            matricula_nova = str(random.randint(100000, 999999))
            aluno = Aluno(
                matricula=matricula_nova,
                nome=request.nome,
                idade=request.idade,
                curso=request.curso,
            )
            self.aluno_repository.save(aluno)
            return CreateAlunoResponse(
                matricula=aluno.matricula,
                nome=aluno.nome,
                idade=aluno.idade,
                curso=aluno.curso,
            )
        except Exception as e:
            raise ValueError(f"Erro ao criar aluno: {e}")


if __name__ == "__main__":
    aluno_repo = AlunoRepository()
    request = CreateAlunoRequest(nome="Maria Oliveira", idade=22, curso="Matemática")
    use_case = CreateAlunoUseCase(aluno_repository=aluno_repo)
    resposta = use_case.execute(request)
    print(f"Aluno criado: {resposta}")
