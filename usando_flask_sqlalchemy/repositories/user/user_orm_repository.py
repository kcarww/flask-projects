from entities.user import User
from repositories.produto.user_repository import UserRepositoryInterface
from dataclasses import dataclass
from app_config import db
from models.user_model import UserModel


@dataclass(slots=True, kw_only=True)
class UserORMRepository(UserRepositoryInterface):
    def __init__(self):
        self.session = db.session

    def find_all(self):
        return [self.to_entity(user) for user in self.session.query(UserModel).all()]

    def find(self, id: int):
        return self.to_entity(self.session.query(UserModel).get(id))

    def create(self, user: User):
        user_model = self.to_model(user)
        self.session.add(user_model)
        self.session.commit()

    def update(self, user: UserModel, id: int):
        user_finded = self.session.query(UserModel).get(id)
        user_finded.nome = user.nome
        user_finded.password = user.password
        self.session.commit()

    def delete(self, id: int):
        self.session.delete(self.session.query(UserModel).get(id))
        self.session.commit()

    def to_entity(self, user_model: UserModel):
        return User(
            id=user_model.id,
            username=user_model.nome,
            password=user_model.password
        )
        
    def to_model(self, user: User):
        return UserModel(
            id=user.id,
            username=user.nome,
            password=user.password
        )
