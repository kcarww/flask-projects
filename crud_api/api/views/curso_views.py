from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entities import curso
from ..services import curso_service


class CursoList(Resource):
    def get(self):
        return 'Olá mundo!'
    
    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            curso_novo = curso.Curso(nome=request.json['nome'], descricao=request.json['descricao'], data_publicacao=request.json['data_publicacao'])
            result = curso_service.cadastrarCurso(curso_novo)
            return make_response(cs.jsonify(result), 201)
 
    
api.add_resource(CursoList, '/cursos')