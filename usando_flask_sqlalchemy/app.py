from app_config import app, db
from flask import request, redirect, url_for, render_template
from use_cases.create_produto import CreateProdutoUseCase
from use_cases.listar_produto import ListProdutoUseCase
from use_cases.delete_produto import DeleteProdutoUseCase
from use_cases.update_produto import UpdateProdutoUseCase
from use_cases.find_produto_by_id import FindProdutoByIdUseCase
from repositories.produto_orm_repository import ProdutoORMRepository
from repositories.produto_in_memory_repository import ProdutoInMemoryRepository
from entities.produto import Produto


@app.route('/lista-produtos', methods=['GET'])
def lista_produtos():
    use_case = ListProdutoUseCase(repo=ProdutoORMRepository())
    produtos = use_case.execute()
    return render_template('lista_produtos.html', produtos=produtos)

@app.route('/produtos', methods=['GET', 'POST'])
def add_produto():
    use_case = CreateProdutoUseCase(repo=ProdutoORMRepository())
    if request.method == 'POST':
        produto = Produto(
            nome=request.form.get('nome'),
            preco=request.form.get('preco'),
            descricao=request.form.get('descricao') 
        )
        
        use_case.execute(produto=produto)
        return redirect(url_for('add_produto'))

    return render_template('add_produto.html')


@app.route('/deletar-produto/<int:id>', methods=['GET'])
def deletar_produto(id):
    use_case = DeleteProdutoUseCase(repo=ProdutoORMRepository())
    use_case.execute(id)
    return redirect(url_for('lista_produtos'))

@app.route('/atualizar-produto/<int:id>', methods=['GET', 'POST'])
def atualizar_produto(id):
    find_use_case = FindProdutoByIdUseCase(repo=ProdutoORMRepository())
    update_use_case = UpdateProdutoUseCase(repo=ProdutoORMRepository())
    produto = find_use_case.execute(id)
    if request.method == 'POST':
        produto.nome = request.form.get('nome')
        produto.preco = request.form.get('preco')
        produto.descricao = request.form.get('descricao')
        update_use_case.execute(produto, id)
        return redirect(url_for('lista_produtos'))

    return render_template('atualizar_produto.html', produto=produto)

if __name__ == '__main__':
    app.run()