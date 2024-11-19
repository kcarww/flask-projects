from dataclasses import dataclass
from uuid import UUID

from core.produto.domain.produto_repository import ProdutoRepository

@dataclass
class GetProdutoRequest:
    id: UUID
    

@dataclass
class GetProdutoResponse:
    id: UUID
    nome: str
    preco: float
    qtd_estoque: int
    
    

class GetProdutoByIdUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository
    
    def execute(self, request: GetProdutoRequest) -> GetProdutoResponse:
        produto = self.repository.get(request.id)
        return GetProdutoResponse(
            id=produto.id,
            nome=produto.nome,
            preco=produto.preco,
            qtd_estoque=produto.qtd_estoque
        )