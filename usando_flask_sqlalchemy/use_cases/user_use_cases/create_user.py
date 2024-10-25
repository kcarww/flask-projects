from dataclasses import dataclass
from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface
from app_config import bcrypt

@dataclass(slots=True, kw_only=True)
class CreateUserUseCase:
    repo: UserRepositoryInterface
    
    def execute(self, user: User) -> User:
        user.password = self.create_password_hash(user.password)
        
        self.repo.create(user)
        return user
    
    def create_password_hash(self, password: str) -> str:
        return bcrypt.generate_password_hash(password).decode('utf-8')
    
