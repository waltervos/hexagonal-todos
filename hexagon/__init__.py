import datetime
from hexagon.driven_ports.repositories import ForGettingCurrentUser, ForPersistingTodos
from hexagon.driven_ports.recipients import ForAlertingAboutDeadlines
from hexagon.models import Todo


class HexagonalTodos:
    def __init__(
        self,
        todo_repo: ForPersistingTodos,
        user_repo: ForGettingCurrentUser = None,
        recipient: ForAlertingAboutDeadlines = None,
    ):
        self._todo_repo = todo_repo
        self._user_repo = user_repo
        self._recipient = recipient

    def view_todos(self):
        current_user = self._user_repo.get_user()
        all_todos = self._todo_repo.load_all()
        return [t for t in all_todos if t.user == current_user]

    def add_todo(self, task, deadline: datetime.date = None):
        current_user = self._user_repo.get_user()
        todo = Todo(task, current_user)
        self._todo_repo.save(todo)

    def notify_for_deadlines(self, date: datetime.date = None):
        if self._recipient != None:
            for todo in self._todo_repo.load_all():
                self._recipient.send(todo)
