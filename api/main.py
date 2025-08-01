from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Arquivo para armazenar os dados dos alunos
DATA_FILE = 'alunos.json'

# Função para carregar dados do arquivo
def carregar_alunos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Função para salvar dados no arquivo
def salvar_alunos(alunos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)

# Função para gerar próxima matrícula
def gerar_matricula():
    alunos = carregar_alunos()
    if not alunos:
        return "2024001"

    matriculas = [int(aluno['matricula']) for aluno in alunos]
    return str(max(matriculas) + 1)

# Função para validar dados do aluno
def validar_aluno(dados):
    erros = []

    if 'nome' not in dados or not dados['nome'].strip():
        erros.append("Nome é obrigatório")

    if 'idade' not in dados:
        erros.append("Idade é obrigatória")
    else:
        try:
            idade = int(dados['idade'])
            if idade < 16 or idade > 100:
                erros.append("Idade deve estar entre 16 e 100 anos")
        except ValueError:
            erros.append("Idade deve ser um número")

    if 'curso' not in dados or not dados['curso'].strip():
        erros.append("Curso é obrigatório")

    return erros

# ROTAS DA API

@app.route('/')
def home():
    return jsonify({
        "mensagem": "API de Alunos",
        "versao": "1.0",
        "endpoints": {
            "GET /alunos": "Listar todos os alunos",
            "GET /alunos/<matricula>": "Buscar aluno por matrícula",
            "POST /alunos": "Cadastrar novo aluno",
            "PUT /alunos/<matricula>": "Atualizar aluno",
            "DELETE /alunos/<matricula>": "Remover aluno"
        }
    })

# GET /alunos - Listar todos os alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = carregar_alunos()
    return jsonify({
        "total": len(alunos),
        "alunos": alunos
    })

# GET /alunos/<matricula> - Buscar aluno específico
@app.route('/alunos/<matricula>', methods=['GET'])
def buscar_aluno(matricula):
    alunos = carregar_alunos()
    aluno = next((a for a in alunos if a['matricula'] == matricula), None)

    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    return jsonify(aluno)

# POST /alunos - Cadastrar novo aluno
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    # Validar dados
    erros = validar_aluno(dados)
    if erros:
        return jsonify({"erros": erros}), 400

    # Carregar alunos existentes
    alunos = carregar_alunos()

    # Criar novo aluno
    novo_aluno = {
        "matricula": gerar_matricula(),
        "nome": dados['nome'].strip(),
        "idade": int(dados['idade']),
        "curso": dados['curso'].strip(),
        "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Adicionar à lista e salvar
    alunos.append(novo_aluno)
    salvar_alunos(alunos)

    return jsonify({
        "mensagem": "Aluno cadastrado com sucesso",
        "aluno": novo_aluno
    }), 201

# PUT /alunos/<matricula> - Atualizar aluno
@app.route('/alunos/<matricula>', methods=['PUT'])
def atualizar_aluno(matricula):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados não fornecidos"}), 400

    # Validar dados
    erros = validar_aluno(dados)
    if erros:
        return jsonify({"erros": erros}), 400

    # Carregar alunos
    alunos = carregar_alunos()

    # Encontrar aluno
    for i, aluno in enumerate(alunos):
        if aluno['matricula'] == matricula:
            # Atualizar dados
            alunos[i].update({
                "nome": dados['nome'].strip(),
                "idade": int(dados['idade']),
                "curso": dados['curso'].strip(),
                "data_atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            salvar_alunos(alunos)
            return jsonify({
                "mensagem": "Aluno atualizado com sucesso",
                "aluno": alunos[i]
            })

    return jsonify({"erro": "Aluno não encontrado"}), 404

# DELETE /alunos/<matricula> - Remover aluno
@app.route('/alunos/<matricula>', methods=['DELETE'])
def remover_aluno(matricula):
    alunos = carregar_alunos()

    # Encontrar e remover aluno
    for i, aluno in enumerate(alunos):
        if aluno['matricula'] == matricula:
            aluno_removido = alunos.pop(i)
            salvar_alunos(alunos)
            return jsonify({
                "mensagem": "Aluno removido com sucesso",
                "aluno": aluno_removido
            })

    return jsonify({"erro": "Aluno não encontrado"}), 404

# Tratamento de erros
@app.errorhandler(404)
def nao_encontrado(error):
    return jsonify({"erro": "Endpoint não encontrado"}), 404

@app.errorhandler(500)
def erro_interno(error):
    return jsonify({"erro": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    print("🚀 Iniciando API de Alunos...")
    print("📚 Endpoints disponíveis:")
    print("   GET    /alunos           - Listar alunos")
    print("   GET    /alunos/<matricula> - Buscar aluno")
    print("   POST   /alunos           - Cadastrar aluno")
    print("   PUT    /alunos/<matricula> - Atualizar aluno")
    print("   DELETE /alunos/<matricula> - Remover aluno")
    print("\n🌐 Acesse: http://localhost:5000")

    app.run(debug=True, host='0.0.0.0', port=5000)
