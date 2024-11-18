from app_config import db

class ProdutoModel(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.String(255), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
