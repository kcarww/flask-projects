from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash
from model.models import Base, Funcionario, Consultor, Supervisor, OrdemServico
from model.execute_tables import get_db



@app.route('/')
def index():
    """Página inicial"""
    return render_template('index.html')

@app.route('/cadastro-funcionario')
def form_cadastro():
    """Exibe o formulário de cadastro"""
    return render_template('cadastro_funcionario.html')

@app.route('/cadastrar_funcionario', methods=['POST'])
def cadastrar_funcionario():
    """Processa o cadastro do funcionário"""
    db = get_db()
    try:
        # Obter dados do formulário
        matricula = request.form['matricula']
        nome = request.form['nome']
        loja = request.form['loja']
        senha = request.form['senha']
        tipo = request.form['tipo']
        
        # Verificar se matrícula já existe
        funcionario_existente = db.query(Funcionario).filter(
            Funcionario.matricula == matricula
        ).first()
        
        if funcionario_existente:
            flash('Matrícula já cadastrada!', 'error')
            return redirect(url_for('form_cadastro'))
        
        # Hash da senha
        senha_hash = generate_password_hash(senha)
        
        # Criar funcionário baseado no tipo
        if tipo == 'consultor':
            novo_funcionario = Consultor(
                matricula=matricula,
                nome=nome,
                loja=loja,
                senha=senha_hash
            )
        elif tipo == 'supervisor':
            novo_funcionario = Supervisor(
                matricula=matricula,
                nome=nome,
                loja=loja,
                senha=senha_hash
            )
        else:
            flash('Tipo de funcionário inválido!', 'error')
            return redirect(url_for('form_cadastro'))
        
        # Salvar no banco
        db.add(novo_funcionario)
        db.commit()
        
        flash(f'{tipo.capitalize()} {nome} cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_funcionarios'))
        
    except Exception as e:
        db.rollback()
        flash(f'Erro ao cadastrar funcionário: {str(e)}', 'error')
        print(f'Erro ao cadastrar funcionário: {str(e)}', 'error')
        return redirect(url_for('form_cadastro'))
    finally:
        db.close()

@app.route('/funcionarios')
def listar_funcionarios():
    """Lista todos os funcionários"""
    db = get_db()
    try:
        funcionarios = db.query(Funcionario).all()
        return render_template('lista_funcionarios.html', funcionarios=funcionarios)
    finally:
        db.close()


@app.route('/editar_funcionario/<int:matricula>')
def editar_funcionario(matricula):
    """Exibe o formulário de edição do funcionário"""
    session = get_db()
    try:
        funcionario = session.query(Funcionario).filter(Funcionario.matricula == matricula).first()
        if funcionario:
            return render_template('editar_funcionario.html', funcionario=funcionario)
        else:
            flash('Funcionário não encontrado!', 'error')
            return redirect(url_for('listar_funcionarios'))
    finally:
        session.close()

@app.route('/atualizar_funcionario', methods=['POST'])
def atualizar_funcionario():
    """Atualiza os dados do funcionário"""
    session = get_db()
    try:
        matricula = request.form['matricula']
        nome = request.form['nome']
        loja = request.form['loja']
        tipo = request.form['tipo']
        
        funcionario = session.query(Funcionario).filter(Funcionario.matricula == matricula).first()
        if funcionario:
            funcionario.nome = nome
            funcionario.loja = loja
            funcionario.tipo = tipo
            session.commit()
            flash('Funcionário atualizado com sucesso!', 'success')
        else:
            flash('Funcionário não encontrado!', 'error')
        return redirect(url_for('listar_funcionarios'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao atualizar funcionário: {str(e)}', 'error')
        return redirect(url_for('listar_funcionarios'))
    finally:
        session.close()

@app.route('/excluir_funcionario/<int:matricula>')
def excluir_funcionario(matricula):
    """Exclui o funcionário"""
    session = get_db()
    try:
        funcionario = session.query(Funcionario).filter(Funcionario.matricula == matricula).first()
        if funcionario:
            session.delete(funcionario)
            session.commit()
            flash('Funcionário excluído com sucesso!', 'success')
        else:
            flash('Funcionário não encontrado!', 'error')
        return redirect(url_for('listar_funcionarios'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao excluir funcionário: {str(e)}', 'error')
        return redirect(url_for('listar_funcionarios'))
    finally:
        session.close()