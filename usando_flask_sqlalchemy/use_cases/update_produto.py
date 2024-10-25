from dataclasses import dataclass
from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface

@dataclass(slots=True, kw_only=True)
class UpdateProdutoUseCase:
    repo: ProdutoRepositoryInterface
    
    def execute(self, produto: Produto, id: int) -> Produto:
        self.repo.update(produto, id)
        return produto