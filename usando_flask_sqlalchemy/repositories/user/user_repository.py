from dataclasses import dataclass
from entities.user import User
from abc import ABC


@dataclass
class UserRepositoryInterface(ABC):
    def find_all(self):
        raise NotImplementedError
    
    def find(self, id: int):
        raise NotImplementedError
    
    def create(self, user: User):
        raise NotImplementedError
    
    def update(self, user: User, id: int):
        raise NotImplementedError
    
    def delete(self, id: int):
        raise NotImplementedError
    
    