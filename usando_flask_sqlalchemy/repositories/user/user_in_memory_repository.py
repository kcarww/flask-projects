from dataclasses import dataclass, field
from entities.user import User
from repositories.produto.user_repository import UserRepositoryInterface
@dataclass(kw_only=True, slots=True)
class UserInMemoryRepository(UserRepositoryInterface):
    items: list = field(default_factory=list)

    def find_all(self):
        return self.items

    def find(self, id: int):
        for user in self.items:
            if user.id == id:
                return user
        return None

    def create(self, user: User):
        self.items.append(user)

    def update(self, user: User):
        for u in self.items:
            if u.id == user.id:
                u.nome = user.nome
                u.preco = user.preco
                u.descricao = user.descricao
                return
        return None
