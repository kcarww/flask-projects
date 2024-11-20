from flask_restful import Resource
from flask import request, jsonify, make_response
from core.produto.infra.produto_orm_repository import ProdutoORMRepository
from core.produto.application.use_cases.create_produto import  *
from core.produto.application.use_cases.delete_produto import *
from core.produto.application.use_cases.get_produto_by_id import *
from core.produto.application.use_cases.list_produto import *
from core.produto.application.use_cases.update_produto import *
from uuid import UUID
from app_config import api
from core.produto.schema.produto_schema import ProdutoSchema

class ProdutoView(Resource):
    def __init__(self):
        self.repository = ProdutoORMRepository()
        self.create_use_case = CreateProdutoUseCase(self.repository)
        self.delete_use_case = DeleteProdutoUseCase(self.repository)
        self.get_by_id_use_case = GetProdutoByIdUseCase(self.repository)
        self.list_use_case = ListProdutoUseCase(self.repository)
        self.update_use_case = UpdateProdutoUseCase(self.repository)
        self.schema = ProdutoSchema()
        self.schema_many = ProdutoSchema(many=True)
    
    def get(self, id: str = None):
        if id:
            produto = self.get_by_id_use_case.execute(GetProdutoRequest(UUID(id)))
            return make_response(self.schema.dump(produto), 200)
        else:
            produtos_response = self.list_use_case.execute(ListProdutoRequest())
            produtos = produtos_response.data
            return make_response(self.schema_many.dump(produtos), 200)
            
            

    def post(self):
        data = self.schema.load(request.json)

        input = CreateProdutoRequest(
            nome=data.nome,
            preco=data.preco,
            qtd_estoque=data.qtd_estoque
            )
        output = self.create_use_case.execute(input)
        return make_response(self.schema.dump(output), 201)
        
    def delete(self, id: str):
        self.delete_use_case.execute(DeleteProdutoRequest(UUID(id)))
        return make_response("", 204)
    
    def put(self, id: str):
        input = UpdateProdutoRequest(
            id=UUID(id),
            nome=request.json['nome'],
            preco=request.json['preco'],
            qtd_estoque=request.json['qtd_estoque']
        )
        
        output = self.update_use_case.execute(input)
        return make_response({
            "id": str(output.id),
            "nome": output.nome,
            "preco": output.preco,
            "qtd_estoque": output.qtd_estoque
        }, 200)
        



api.add_resource(ProdutoView, '/produtos', '/produtos/<string:id>')