from dataclasses import dataclass
from flask_login import UserMixin

@dataclass(slots=True)
class User(UserMixin):
    id: int = None
    username: str = None
    password: str = None
    
    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password})'
    
    