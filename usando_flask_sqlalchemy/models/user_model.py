from app_config import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)