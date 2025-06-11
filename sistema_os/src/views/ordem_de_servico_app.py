from flask import render_template, request, redirect, url_for, flash, make_response
from app import app
from model.models import Funcionario, OrdemServico
from model.execute_tables import get_db
from fpdf import FPDF

@app.route('/ordens_servico')
def listar_ordens_servico():
    """Lista todas as ordens de serviço"""
    session = get_db()
    try:
        ordens = session.query(OrdemServico).all()
        return render_template('lista_ordens_servico.html', ordens=ordens)
    finally:
        session.close()

@app.route('/nova_ordem_servico')
def form_nova_ordem_servico():
    """Exibe o formulário para criar uma nova ordem de serviço"""
    session = get_db()
    try:
        funcionarios = session.query(Funcionario).all()
        return render_template('nova_ordem_servico.html', funcionarios=funcionarios)
    finally:
        session.close()

@app.route('/criar_ordem_servico', methods=['POST'])
def criar_ordem_servico():
    """Cria uma nova ordem de serviço"""
    session = get_db()
    try:
        data = request.form['data']
        problema = request.form['problema']
        matricula_funcionario = request.form['matricula_funcionario']
        
        nova_ordem = OrdemServico(
            data=data,
            problema=problema,
            matricula_funcionario=matricula_funcionario
        )
        session.add(nova_ordem)
        session.commit()
        flash('Ordem de serviço criada com sucesso!', 'success')
        return redirect(url_for('listar_ordens_servico'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao criar ordem de serviço: {str(e)}', 'error')
        return redirect(url_for('form_nova_ordem_servico'))
    finally:
        session.close()

@app.route('/editar_ordem_servico/<int:codigo>')
def editar_ordem_servico(codigo):
    """Exibe o formulário de edição da ordem de serviço"""
    session = get_db()
    try:
        ordem = session.query(OrdemServico).filter(OrdemServico.codigo == codigo).first()
        funcionarios = session.query(Funcionario).all()
        if ordem:
            return render_template('editar_ordem_servico.html', ordem=ordem, funcionarios=funcionarios)
        else:
            flash('Ordem de serviço não encontrada!', 'error')
            return redirect(url_for('listar_ordens_servico'))
    finally:
        session.close()

@app.route('/atualizar_ordem_servico', methods=['POST'])
def atualizar_ordem_servico():
    """Atualiza os dados da ordem de serviço"""
    session = get_db()
    try:
        codigo = request.form['codigo']
        data = request.form['data']
        problema = request.form['problema']
        solucao = request.form['solucao']
        status = request.form['status']
        matricula_funcionario = request.form['matricula_funcionario']
        
        ordem = session.query(OrdemServico).filter(OrdemServico.codigo == codigo).first()
        if ordem:
            ordem.data = data
            ordem.problema = problema
            ordem.solucao = solucao
            ordem.status = status
            ordem.matricula_funcionario = matricula_funcionario
            session.commit()
            flash('Ordem de serviço atualizada com sucesso!', 'success')
        else:
            flash('Ordem de serviço não encontrada!', 'error')
        return redirect(url_for('listar_ordens_servico'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao atualizar ordem de serviço: {str(e)}', 'error')
        return redirect(url_for('listar_ordens_servico'))
    finally:
        session.close()

@app.route('/excluir_ordem_servico/<int:codigo>')
def excluir_ordem_servico(codigo):
    """Exclui a ordem de serviço"""
    session = get_db()
    try:
        ordem = session.query(OrdemServico).filter(OrdemServico.codigo == codigo).first()
        if ordem:
            session.delete(ordem)
            session.commit()
            flash('Ordem de serviço excluída com sucesso!', 'success')
        else:
            flash('Ordem de serviço não encontrada!', 'error')
        return redirect(url_for('listar_ordens_servico'))
    except Exception as e:
        session.rollback()
        flash(f'Erro ao excluir ordem de serviço: {str(e)}', 'error')
        return redirect(url_for('listar_ordens_servico'))
    finally:
        session.close()


@app.route('/ordem_servico_pdf/<int:codigo>')
def ordem_servico_pdf(codigo):
    """Gera um PDF da ordem de serviço usando FPDF"""
    session = get_db()
    try:
        ordem = session.query(OrdemServico).filter(OrdemServico.codigo == codigo).first()
        if not ordem:
            flash('Ordem de serviço não encontrada!', 'error')
            return redirect(url_for('listar_ordens_servico'))

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"Ordem de Serviço #{ordem.codigo}", ln=1, align="C")
        pdf.cell(200, 10, txt=f"Data: {ordem.data}", ln=1)
        pdf.cell(200, 10, txt=f"Funcionário: {ordem.funcionario.nome}", ln=1)
        pdf.cell(200, 10, txt=f"Status: {ordem.status}", ln=1)
        pdf.cell(200, 10, txt=f"Problema: {ordem.problema}", ln=1)
        pdf.cell(200, 10, txt=f"Solução: {ordem.solucao}", ln=1)

        response = make_response(pdf.output(dest='S').encode('latin-1'))
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'inline; filename=ordem_servico_{codigo}.pdf'
        return response
    finally:
        session.close()