from flask import Flask, render_template, request, redirect, session, flash
from models.usuario import Usuario
from repositories.usuario_mysql_repository import UsuarioMySQLRepository
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4

app = Flask(__name__)
app.secret_key = 'secret'
usuario_repository = UsuarioMySQLRepository()




@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/validar_cadastro', methods=['POST', 'GET'])
def validar_cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        id = str(uuid4())
        senha_hash = generate_password_hash(
            senha,
            method='pbkdf2:sha256',
            salt_length=16
        )
        usuario = Usuario(id=id, nome=nome, email=email, senha=senha_hash)
        usuario_repository.create(usuario)
        return redirect('/usuarios')  
    return redirect('/usuarios')       

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = usuario_repository.find_by_email(email)
        if usuario and check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash('Login realizado com sucesso!', 'success')
            return redirect('/usuarios')
        else:
            flash('E-mail ou senha inválidos.', 'danger')
            return redirect('/login')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/usuarios')
def listar_usuarios():
    if 'usuario_id' not in session:
        return redirect('/login')
    usuarios = usuario_repository.find_all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/excluir/<usuario_id>', methods=['POST'])
def excluir_usuario(usuario_id):
    if 'usuario_id' not in session:
        return redirect('/login')
    usuario_repository.delete(usuario_id)
    flash('Usuário excluído com sucesso!', 'success')
    return redirect('/usuarios')

@app.route('/usuarios/editar/<usuario_id>', methods=['GET'])
def editar_usuario(usuario_id):
    if 'usuario_id' not in session:
        return redirect('/login')
    usuario = usuario_repository.find(usuario_id)
    if not usuario:
        flash('Usuário não encontrado.', 'danger')
        return redirect('/usuarios')
    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/usuarios/editar/<usuario_id>', methods=['POST'])
def atualizar_usuario(usuario_id):
    if 'usuario_id' not in session:
        return redirect('/login')
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    usuario = usuario_repository.find(usuario_id)
    if not usuario:
        flash('Usuário não encontrado.', 'danger')
        return redirect('/usuarios')

    if senha:
        senha_hash = generate_password_hash(senha)
    else:
        senha_hash = usuario.senha

    usuario_atualizado = Usuario(id=usuario_id, nome=nome, email=email, senha=senha_hash)
    usuario_repository.update(usuario_atualizado)
    flash('Usuário atualizado com sucesso!', 'success')
    return redirect('/usuarios')

if __name__ == '__main__':
    app.run(debug=True)