from dataclasses import dataclass
from uuid import UUID

from core.produto.domain.produto import Produto
from core.produto.domain.produto_repository import ProdutoRepository


@dataclass
class CreateProdutoRequest:
    nome: str
    preco: float
    qtd_estoque: int


@dataclass
class CreateProdutoResponse:
    id: UUID
    nome: str
    preco: float
    qtd_estoque: int


class CreateProdutoUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository

    def execute(self, request: CreateProdutoRequest) -> CreateProdutoResponse:
        produto = Produto(
            nome=request.nome,
            preco=request.preco,
            qtd_estoque=request.qtd_estoque
        )
        
        self.repository.add(produto)
        return CreateProdutoResponse(
            id=produto.id,
            nome=produto.nome,
            preco=produto.preco,
            qtd_estoque=produto.qtd_estoque
        )
