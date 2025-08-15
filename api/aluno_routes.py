# src/aluno/infrastructure/routes/aluno_routes.py
from flask import Blueprint, request, jsonify
from src.aluno.application.use_cases.create.create_aluno_use_case import CreateAlunoUseCase
from src.aluno.application.use_cases.list.list_alunos_use_case import ListAlunosUseCase
from src.aluno.application.use_cases.get.get_aluno_use_case import GetAlunoUseCase
from src.aluno.application.use_cases.update.update_aluno_use_case import UpdateAlunoUseCase
from src.aluno.application.use_cases.delete.delete_aluno_use_case import DeleteAlunoUseCase
from src.aluno.infrastructure.aluno_repository import AlunoRepository

# Criar blueprint para as rotas de aluno
aluno_bp = Blueprint('alunos', __name__)

# Instanciar dependências (em projetos maiores, use DI container)
aluno_repository = AlunoRepository()
create_aluno_use_case = CreateAlunoUseCase(aluno_repository)
list_alunos_use_case = ListAlunosUseCase(aluno_repository)
get_aluno_use_case = GetAlunoUseCase(aluno_repository)
update_aluno_use_case = UpdateAlunoUseCase(aluno_repository)
delete_aluno_use_case = DeleteAlunoUseCase(aluno_repository)

@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    """Lista todos os alunos"""
    try:
        alunos = list_alunos_use_case.execute()
        return jsonify([aluno.__dict__ for aluno in alunos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/alunos/<matricula>', methods=['GET'])
def buscar_aluno(matricula):
    """Busca um aluno por matrícula"""
    try:
        aluno = get_aluno_use_case.execute(matricula)
        if aluno:
            return jsonify(aluno.__dict__), 200
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/alunos', methods=['POST'])
def criar_aluno():
    """Cria um novo aluno"""
    try:
        dados = request.get_json()
        
        if not dados:
            return jsonify({'error': 'Dados não fornecidos'}), 400
            
        response = create_aluno_use_case.execute(
            nome=dados.get('nome'),
            idade=dados.get('idade'),
            curso=dados.get('curso')
        )
        
        return jsonify(response.__dict__), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/alunos/<matricula>', methods=['PUT'])
def atualizar_aluno(matricula):
    """Atualiza um aluno existente"""
    try:
        dados = request.get_json()
        
        if not dados:
            return jsonify({'error': 'Dados não fornecidos'}), 400
            
        aluno_atualizado = update_aluno_use_case.execute(
            matricula=matricula,
            nome=dados.get('nome'),
            idade=dados.get('idade'),
            curso=dados.get('curso')
        )
        
        if aluno_atualizado:
            return jsonify(aluno_atualizado.__dict__), 200
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@aluno_bp.route('/alunos/<matricula>', methods=['DELETE'])
def deletar_aluno(matricula):
    """Deleta um aluno"""
    try:
        sucesso = delete_aluno_use_case.execute(matricula)
        
        if sucesso:
            return jsonify({'message': 'Aluno deletado com sucesso'}), 200
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
