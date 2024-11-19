from dataclasses import dataclass, field
from uuid import UUID, uuid4
@dataclass(kw_only=True)
class Produto:
    id: UUID = field(default_factory=uuid4)
    nome: str
    preco: float
    qtd_estoque: int
    
    def __repr__(self) -> str:
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, qtd_estoque={self.qtd_estoque})"