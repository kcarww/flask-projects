from dataclasses import dataclass
from uuid import UUID

from core.produto.domain.produto_repository import ProdutoRepository

@dataclass
class DeleteProdutoRequest:
    id: UUID
    
    
class DeleteProdutoUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository
        
    def execute(self, request: DeleteProdutoRequest) -> None:
        self.repository.delete(request.id)