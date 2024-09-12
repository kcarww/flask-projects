# pylint: disable=E0401,C0116,C0114,C0103,C0301,
import urllib.request
import json
from flask import Flask, render_template, request
app = Flask(__name__)


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


@app.route('/filmes')
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13"

    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])
    # return jsondata


if __name__ == '__main__':
    app.run(debug=True)
