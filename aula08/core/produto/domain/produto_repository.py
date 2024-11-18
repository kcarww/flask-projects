from abc import ABC, abstractmethod
from uuid import UUID
from core.produto.domain.produto import Produto

class ProdutoRepository(ABC):
    @abstractmethod
    def add(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def get(self, produto_id: UUID) -> Produto:
        pass

    @abstractmethod
    def list(self) -> list[Produto]:
        pass

    @abstractmethod
    def update(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def delete(self, produto_id: UUID) -> None:
        pass