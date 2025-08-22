from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def save(self, entity):
        pass
