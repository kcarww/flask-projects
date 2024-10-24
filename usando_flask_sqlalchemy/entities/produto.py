from dataclasses import dataclass

@dataclass(slots=True)
class Produto:
    id: int = None
    nome: str = None
    descricao: str = None
    preco: float = None
    
    def __repr__(self):
        return f'Produto(id={self.id}, nome={self.nome}, descricao={self.descricao}, preco={self.preco})'