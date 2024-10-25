from dataclasses import dataclass
from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface

@dataclass(slots=True, kw_only=True)
class UpdateProdutoUseCase:
    repo: ProdutoRepositoryInterface
    
    def execute(self, produto: Produto, id: int) -> Produto:
        produto = self.repo.find(id)
        self.repo.update(produto)
        return produto