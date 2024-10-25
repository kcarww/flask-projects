from dataclasses import dataclass

@dataclass(slots=True)
class User:
    id: int = None
    username: str = None
    password: str = None
    
    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password})'
    
    