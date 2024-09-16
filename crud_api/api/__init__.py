from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .views import curso_views
from .models import curso_model