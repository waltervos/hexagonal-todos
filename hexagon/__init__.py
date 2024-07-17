from hexagon.driven_ports.repositories import ForGettingCurrentUser, ForPersistingTodos
from hexagon.models import Todo


class HexagonalTodos:
    def __init__(self, todo_repo: ForPersistingTodos, user_repo: ForGettingCurrentUser = None):
        self._todo_repo = todo_repo
        self._user_repo = user_repo

    def view_todos(self):
        current_user = self._user_repo.get_user()
        all_todos = self._todo_repo.load_all()
        return [t for t in all_todos if t.user == current_user]
    
    def add_todo(self, task):
        current_user = self._user_repo.get_user()
        todo = Todo(task, current_user)
        self._todo_repo.save(todo)
