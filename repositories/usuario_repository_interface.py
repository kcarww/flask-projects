from abc import ABC, abstractmethod
from models.usuario import Usuario

class UsuarioRepositoryInterface(ABC):
    @abstractmethod
    def create(self, usuario: Usuario):
        """Create a new user."""
        pass

    @abstractmethod
    def find(self, usuario_id: str):
        """Retrieve a user by their ID."""
        pass

    @abstractmethod
    def update(self, usuario: Usuario):
        """Update an existing user."""
        pass

    @abstractmethod
    def delete(self, usuario_id: str):
        """Delete a user by their ID."""
        pass

    @abstractmethod
    def find_all(self):
        """List all users."""
        pass