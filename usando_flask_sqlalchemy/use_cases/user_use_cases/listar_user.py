from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class ListUserUseCase:
    repo: UserRepositoryInterface

    def execute(self) -> list[User]:
        return self.repo.find_all()