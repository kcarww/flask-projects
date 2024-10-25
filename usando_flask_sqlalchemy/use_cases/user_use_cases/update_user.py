from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class UpdateUserUseCase:
    repo: UserRepositoryInterface
    
    def execute(self, user: User, id: int) -> User:
        self.repo.update(user, id)
        return user