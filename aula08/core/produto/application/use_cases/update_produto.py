from dataclasses import dataclass
from uuid import UUID
from core.produto.domain.produto_repository import ProdutoRepository

@dataclass
class UpdateProdutoRequest:
    id: UUID
    nome: str
    preco: float
    qtd_estoque: int
    
@dataclass
class UpdateProdutoResponse:
    id: UUID
    nome: str
    preco: float
    qtd_estoque: int



class UpdateProdutoUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository
        
    def execute(self, request: UpdateProdutoRequest) -> UpdateProdutoResponse:
        
        produto = self.repository.get(request.id)
        produto.nome = request.nome
        produto.preco = request.preco
        produto.qtd_estoque = request.qtd_estoque
        
        self.repository.update(produto)
        return UpdateProdutoResponse(
            id=produto.id,
            nome=produto.nome,
            preco=produto.preco,
            qtd_estoque=produto.qtd_estoque
        )