from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class FindUserByIdUseCase:
    repo: UserRepositoryInterface

    def execute(self, id: int) -> User:
        return self.repo.find(id)