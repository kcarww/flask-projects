from dataclasses import dataclass
from uuid import UUID

from core.produto.domain.produto_repository import ProdutoRepository

@dataclass
class ListProdutoRequest:
    pass
    

@dataclass
class ProdutoResponse:
    id: UUID
    nome: str
    preco: float
    qtd_estoque: int
    
@dataclass
class ListProdutoResponse:
    data: list[ProdutoResponse]
    

class ListProdutoUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository
        
    def execute(self, request: ListProdutoRequest) -> ListProdutoResponse:
        produtos = self.repository.list()
        return ListProdutoResponse(
            data = [
                ProdutoResponse(
                    id=produto.id,
                    nome=produto.nome,
                    preco=produto.preco,
                    qtd_estoque=produto.qtd_estoque
                )
                for produto in produtos
            ]
        )