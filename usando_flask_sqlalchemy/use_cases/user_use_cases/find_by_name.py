from entities.user import User
from repositories.user.user_repository import UserRepositoryInterface
from dataclasses import dataclass

@dataclass(slots=True, kw_only=True)
class FindUserByUsernameUseCase:
    repo: UserRepositoryInterface

    def execute(self, username: str) -> User:
        return self.repo.find_by_username(username)