from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface
from dataclasses import dataclass
from app_config import db

@dataclass(slots=True, kw_only=True)
class ProdutoORMRepository(ProdutoRepositoryInterface):
    def __init__(self):
        self.session = db.session

    def find_all(self):
        return self.session.query(Produto).all()

    def find(self, id: int):
        return self.session.query(Produto).get(id)

    def create(self, produto: Produto):
        self.session.add(produto)
        self.session.commit()

    def update(self, produto: Produto):
        self.session.add(produto)
        self.session.commit()

    def delete(self, id: int):
        produto = self.find(id)
        self.session.delete(produto)
        self.session.commit()