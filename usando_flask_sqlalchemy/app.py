from app_config import app, db
from flask import request, redirect, url_for, render_template
from use_cases.create_produto import CreateProdutoUseCase
from use_cases.listar_produto import ListProdutoUseCase
from repositories.produto_orm_repository import ProdutoORMRepository
from repositories.produto_in_memory_repository import ProdutoInMemoryRepository
from entities.produto import Produto



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
    list_use_case = ListProdutoUseCase(repo=ProdutoORMRepository())
    produtos = list_use_case.execute()
    return render_template('add_produto.html', produtos=produtos)

if __name__ == '__main__':
    app.run()