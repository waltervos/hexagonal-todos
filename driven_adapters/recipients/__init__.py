from hexagon.driven_ports.recipients import ForAlertingAboutDeadlines
from hexagon.models import Todo


class InMemoryDeadlineAlertRecipient(ForAlertingAboutDeadlines):
    def __init__(self) -> None:
        self.received_alerts = []
        self.received_alerts_by_user = {}

    def send(self, todo: Todo) -> None:
        self.received_alerts_by_user[todo.user] = [todo.task]
