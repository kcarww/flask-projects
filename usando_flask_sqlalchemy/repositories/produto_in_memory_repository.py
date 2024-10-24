from dataclasses import dataclass, field
from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface
@dataclass(kw_only=True, slots=True)
class ProdutoInMemoryRepository(ProdutoRepositoryInterface):
    items: list = field(default_factory=list)

    def find_all(self):
        return self.items

    def find(self, id: int):
        for produto in self.items:
            if produto.id == id:
                return produto
        return None

    def create(self, produto: Produto):
        self.items.append(produto)

    def update(self, produto: Produto):
        for p in self.items:
            if p.id == produto.id:
                p.nome = produto.nome
                p.preco = produto.preco
                p.descricao = produto.descricao
                return
        return None
