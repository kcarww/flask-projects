from src.geral.infrastructure.repository_interface import RepositoryInterface
from src.curso.domain.curso import Curso
import json


class CursoRepository(RepositoryInterface):
    def carregar_cursos(self):
        with open("cursos.json", "r") as file:
            return json.load(file)

    def save(self, curso: Curso):
        cursos = self.carregar_cursos()
        cursos.append(
            {
                "id": curso.id,
                "nome": curso.nome,
                "descricao": curso.descricao,
                "horas": curso.horas,
            }
        )

        with open("cursos.json", "w") as file:
            json.dump(cursos, file, indent=4)


if __name__ == "__main__":
    repo = CursoRepository()
    curso = Curso(
        id=2,
        nome="Curso Avançado de Python",
        descricao="Aprofunde seus conhecimentos em Python com este curso avançado.",
        horas=300,
    )
    repo.save(curso)
