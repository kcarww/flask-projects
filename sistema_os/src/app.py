from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

from views.funcionario_app import *
from views.ordem_de_servico_app import *

if __name__ == '__main__':
    app.run(debug=True)