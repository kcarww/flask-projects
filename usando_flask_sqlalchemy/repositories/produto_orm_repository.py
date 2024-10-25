from entities.produto import Produto
from repositories.produto_repository import ProdutoRepositoryInterface
from dataclasses import dataclass
from app_config import db
from models.produto_model import Produto as ProdutoModel


@dataclass(slots=True, kw_only=True)
class ProdutoORMRepository(ProdutoRepositoryInterface):
    def __init__(self):
        self.session = db.session

    def find_all(self):
        return [self.to_entity(produto) for produto in self.session.query(ProdutoModel).all()]

    def find(self, id: int):
        return self.to_entity(self.session.query(ProdutoModel).get(id))

    def create(self, produto: Produto):
        produto_model = self.to_model(produto)
        self.session.add(produto_model)
        self.session.commit()

    def update(self, produto: Produto):
        self.session.add(produto)
        self.session.commit()

    def delete(self, id: int):
        self.session.delete(self.session.query(ProdutoModel).get(id))
        self.session.commit()

    def to_entity(self, produto_model: ProdutoModel):
        return Produto(
            id=produto_model.id,
            nome=produto_model.nome,
            descricao=produto_model.descricao,
            preco=produto_model.preco
        )
        
    def to_model(self, produto: Produto):
        return ProdutoModel(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco
        )
