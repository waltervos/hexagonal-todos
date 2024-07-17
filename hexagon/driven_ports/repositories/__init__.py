from abc import ABC, abstractmethod

from hexagon.models import Todo


class ForPersistingTodos(ABC):
    @abstractmethod
    def save(self, todo: Todo):
        pass

    @abstractmethod
    def load_all(self) -> list[Todo]:
        pass

class ForGettingCurrentUser(ABC):
    @abstractmethod
    def get_user(self):
        pass