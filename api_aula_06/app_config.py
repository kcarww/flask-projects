from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.aluno import Aluno
