from dataclasses import dataclass
from entities.produto import Produto
from repositories.produto.produto_repository import ProdutoRepositoryInterface


@dataclass(slots=True, kw_only=True)
class DeleteProdutoUseCase:
    repo: ProdutoRepositoryInterface
    
    def execute(self, id: int) -> Produto:
        self.repo.delete(id)
        return None