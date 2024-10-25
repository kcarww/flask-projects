from entities.produto import Produto
from repositories.produto.produto_repository import ProdutoRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class ListProdutoUseCase:
    repo: ProdutoRepositoryInterface

    def execute(self) -> list[Produto]:
        return self.repo.find_all()