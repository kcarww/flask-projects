# pylint: disable=E0401,C0116,C0114,C0103
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
@app.route('/form', methods=['GET','POST'])
def cadastrarFruta():
    if request.method == 'POST':
        if request.form.get('fruta'):
            frutas.append(request.form.get('fruta'))
    return render_template('formulario.html', frutas=frutas)


if __name__ == '__main__':
    app.run(debug=True)
