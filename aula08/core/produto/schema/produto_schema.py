from app_config import ma
from core.produto.model.produto_model import ProdutoModel
from marshmallow import fields

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProdutoModel
        load_instance = True
        fields = ("id", "nome", "qtd_estoque", "preco")
        
    id = fields.UUID(dump_only=True) 
    nome = fields.String(required=True)
    qtd_estoque = fields.Integer(required=True)
    preco = fields.Float(required=True)