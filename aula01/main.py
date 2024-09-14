# pylint: disable=E0401,C0116,C0114,C0115,C0103,C0301,W0311,E0001
import urllib.request
import json
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/escola'

db = SQLAlchemy(app)

class Cursos(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255))
    ch = db.Column(db.Integer)

    
    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch
@app.route('/')
def main():
    produtos = [
        'mouse', 'teclado', 'monitor'
    ]
    return render_template('index.html', produtos=produtos)


@app.route('/alunos')
def getAlunos():
    alunos = {
        "Jonas": 9.0,
        "Elias": 10.0,
        "marcos": 8.6
    }
    return render_template('alunos.html', alunos=alunos)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


frutas = []


@app.route('/form', methods=['GET', 'POST'])
def cadastrarFruta():
    if request.method == 'POST':
        if request.form.get('fruta'):
            frutas.append(request.form.get('fruta'))
    return render_template('formulario.html', frutas=frutas)


@app.route('/filmes/<filtro>')
def filmes(filtro):
    if filtro == 'populares':
	    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"
    elif filtro == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"
    elif filtro == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"
    elif filtro == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=3ddc9b92db4de6c6559569c67bd88a13"
    elif filtro == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"

    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])
    # return jsondata
    
    
@app.route('/cursos')
def getCursos():
    cursos = Cursos.query.all()
    return render_template('cursos.html', cursos=cursos)


@app.route('/add-curso', methods=['GET', 'POST'])
def createCurso():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        ch = request.form.get('ch')

        curso = Cursos(nome, descricao, ch)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('getCursos'))
    return render_template('add-curso.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
