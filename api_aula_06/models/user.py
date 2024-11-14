from app_config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    
    
    def __repr__(self) -> str:
        return f"<User> - {self.username} - {self.password}" 

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }