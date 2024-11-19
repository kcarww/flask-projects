from core.produto.domain.produto_repository import ProdutoRepository
from core.produto.domain.produto import Produto
from uuid import UUID

class InMemoryProdutoRepository(ProdutoRepository):
    def __init__(self, produtos: list[Produto] = []):
        self.produtos = produtos
        
    def add(self, produto: Produto) -> Produto:
        self.produtos.append(produto)
        return produto
    
    def get(self, produto_id: UUID) -> Produto:
        for produto in self.produtos:
            if produto.id == produto_id:
                return produto
    
    def list(self) -> list[Produto]:
        return self.produtos
    
    def update(self, produto: Produto) -> Produto:
        produto_old = self.get(produto.id)
        produto_old.nome = produto.nome
        produto_old.preco = produto.preco
        return produto_old
    
    def delete(self, produto_id: UUID) -> Produto:
        produto = self.get(produto_id)
        self.produtos.remove(produto)
        return produto