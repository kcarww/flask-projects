from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
app.secret_key = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'another_super_secret_key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
ma = Marshmallow(app)


from core.produto.model.produto_model import ProdutoModel
from core.produto.view.produto_view import ProdutoView
# from core.produto.schema.produto_schema import ProdutoSchema
