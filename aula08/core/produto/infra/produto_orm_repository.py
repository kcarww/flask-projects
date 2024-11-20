from uuid import UUID
from core.produto.domain.produto import Produto
from core.produto.domain.produto_repository import ProdutoRepository
from core.produto.model.produto_model import ProdutoModel
from app_config import db

class ProdutoORMRepository(ProdutoRepository):
    def __init__(self, model: ProdutoModel = ProdutoModel):
        self.model = model
        
    def add(self, produto: Produto):
        db.session.add(ProdutoMapper.to_model(produto))
        db.session.commit()
        
    def get(self, id: UUID) -> Produto:
        produto = db.session.query(self.model).get(str(id))
        return ProdutoMapper.to_domain(produto)
    
    def list(self) -> list[Produto]:
        produtos = db.session.query(self.model).all()
        return [ProdutoMapper.to_domain(produto) for produto in produtos]
    
    def update(self, produto: Produto) -> Produto:
        produto_new = db.session.query(self.model).filter_by(id=str(produto.id)).first()
        produto_new.nome = produto.nome
        produto_new.preco = produto.preco
        produto_new.qtd_estoque = produto.qtd_estoque
        db.session.commit()
        return ProdutoMapper.to_domain(produto_new)
    
    def delete(self, id: UUID):
        produto = db.session.query(self.model).get(str(id))
        db.session.delete(produto)
        db.session.commit()
    
    
    
class ProdutoMapper:
    @staticmethod
    def to_domain(model: ProdutoModel) -> Produto:
        return Produto(
            id=UUID(model.id),
            nome=model.nome,
            preco=model.preco,
            qtd_estoque=model.qtd_estoque
        )
        
    @staticmethod
    def to_model(produto: Produto) -> ProdutoModel:
        return ProdutoModel(
            id=str(produto.id),
            nome=produto.nome,
            preco=produto.preco,
            qtd_estoque=produto.qtd_estoque
        )
    