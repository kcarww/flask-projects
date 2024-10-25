from app_config import app, db, login_manager
from flask import request, redirect, url_for, render_template, flash
from use_cases.produto_use_cases.create_produto import CreateProdutoUseCase
from use_cases.produto_use_cases.listar_produto import ListProdutoUseCase
from use_cases.produto_use_cases.delete_produto import DeleteProdutoUseCase
from use_cases.produto_use_cases.update_produto import UpdateProdutoUseCase
from use_cases.produto_use_cases.find_produto_by_id import FindProdutoByIdUseCase
from repositories.produto.produto_orm_repository import ProdutoORMRepository
from repositories.user.user_orm_repository import UserORMRepository
from entities.produto import Produto
from entities.user import User
from use_cases.user_use_cases.create_user import CreateUserUseCase
from use_cases.user_use_cases.find_by_name import FindUserByUsernameUseCase
from use_cases.user_use_cases.verify_user_password import verify_user_password
from flask_login import login_required, login_user


login_manager.login_view = 'login'
login_manager.login_message = "Você precisa fazer login para acessar esta página."

@app.route('/lista-produtos', methods=['GET'])
@login_required
def lista_produtos():
    use_case = ListProdutoUseCase(repo=ProdutoORMRepository())
    produtos = use_case.execute()
    return render_template('lista_produtos.html', produtos=produtos)

@app.route('/produtos', methods=['GET', 'POST'])
@login_required
def add_produto():
    use_case = CreateProdutoUseCase(repo=ProdutoORMRepository())
    if request.method == 'POST':
        produto = Produto(
            nome=request.form.get('nome'),
            preco=request.form.get('preco'),
            descricao=request.form.get('descricao') 
        )
        
        use_case.execute(produto=produto)
        return redirect(url_for('lista_produtos'))

    return render_template('add_produto.html')


@app.route('/deletar-produto/<int:id>', methods=['GET'])
@login_required
def deletar_produto(id):
    use_case = DeleteProdutoUseCase(repo=ProdutoORMRepository())
    use_case.execute(id)
    return redirect(url_for('lista_produtos'))

@app.route('/atualizar-produto/<int:id>', methods=['GET', 'POST'])
@login_required
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


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    use_case = CreateUserUseCase(repo=UserORMRepository())
    if request.method == 'POST':
        user = User(
            username=request.form.get('username').lower(),
            password=request.form.get('password')
        )
        
        use_case.execute(user=user)
        return redirect(url_for('add_user'))

    return render_template('add_user.html')


@login_manager.user_loader
def load_user(user_id):
    repo = UserORMRepository()
    return repo.find(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    use_case = FindUserByUsernameUseCase(repo=UserORMRepository())
    if request.method == 'POST':
        username = request.form.get('username').lower()
        password = request.form.get('password')
        user = use_case.execute(username)
        if user and verify_user_password(user.password, password):
            login_user(user) 
            return redirect(url_for('lista_produtos'))
        
        flash("Usuário ou senha incorretos.", "error")
        return redirect(url_for('login'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run()