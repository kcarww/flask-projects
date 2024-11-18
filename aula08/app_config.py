from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow



app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'another_super_secret_key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
ma = Marshmallow(app)


from core.produto.model.produto_model import ProdutoModel
