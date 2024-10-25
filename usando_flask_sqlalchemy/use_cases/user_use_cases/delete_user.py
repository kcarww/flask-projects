from dataclasses import dataclass
from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface


@dataclass(slots=True, kw_only=True)
class DeleteUserUseCase:
    repo: UserRepositoryInterface
    
    def execute(self, id: int) -> User:
        self.repo.delete(id)
        return None