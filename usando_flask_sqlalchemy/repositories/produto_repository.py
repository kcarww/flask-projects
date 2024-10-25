from dataclasses import dataclass
from entities.produto import Produto
from abc import ABC


@dataclass
class ProdutoRepositoryInterface(ABC):
    def find_all(self):
        raise NotImplementedError
    
    def find(self, id: int):
        raise NotImplementedError
    
    def create(self, produto: Produto):
        raise NotImplementedError
    
    def update(self, produto: Produto, id: int):
        raise NotImplementedError
    
    def delete(self, id: int):
        raise NotImplementedError
    
    