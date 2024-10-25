from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class FindProdutoByIdUseCase:
    repo: ProdutoRepositoryInterface

    def execute(self, id: int) -> Produto:
        return self.repo.find(id)