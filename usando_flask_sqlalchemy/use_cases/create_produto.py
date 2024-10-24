from dataclasses import dataclass
from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface


@dataclass(slots=True, kw_only=True)
class CreateProdutoUseCase:
    repo: ProdutoRepositoryInterface
    
    def execute(self, produto: Produto) -> Produto:
        self.repo.create(produto)
        return produto