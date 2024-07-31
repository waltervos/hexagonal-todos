from abc import ABC

from hexagon.models import Todo


class ForAlertingAboutDeadlines(ABC):
    def send(self, todo: Todo) -> None:
        pass
