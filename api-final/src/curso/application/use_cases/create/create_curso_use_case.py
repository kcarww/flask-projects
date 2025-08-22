from src.geral.infrastructure.repository_interface import RepositoryInterface
from src.curso.infrastructure.curso_repository import CursoRepository
from src.curso.domain.curso import Curso
from dataclasses import dataclass
from random import randint


@dataclass
class CreateCursoResponse:
    id: int
    nome: str
    descricao: str
    horas: int


@dataclass
class CreateCursoRequest:
    nome: str
    descricao: str
    horas: int


class CreateCursoUseCase:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def execute(self, request: CreateCursoRequest) -> CreateCursoResponse:
        id = randint(3, 10000)
        try:
            novo_curso = Curso(
                id=id,
                nome=request.nome,
                descricao=request.descricao,
                horas=request.horas,
            )
            self.repository.save(novo_curso)
            return CreateCursoResponse(
                id=novo_curso.id,
                nome=novo_curso.nome,
                descricao=novo_curso.descricao,
                horas=novo_curso.horas,
            )
        except Exception as e:
            raise Exception(f"Erro ao criar curso: {e}") from e


if __name__ == "__main__":
    repository = CursoRepository()
    use_case = CreateCursoUseCase(repository)
    request = CreateCursoRequest(
        nome="javascript Avançado", descricao="Curso avançado de javascript", horas=40
    )
    response = use_case.execute(request)
    print(response)
