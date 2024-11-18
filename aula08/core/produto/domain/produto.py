from dataclasses import dataclass, field
from uuid import UUID
@dataclass(kw_only=True)
class Produto:
    id: UUID = field(default_factory=UUID)
    nome: str
    preco: float
    qtd_estoque: int
    
    