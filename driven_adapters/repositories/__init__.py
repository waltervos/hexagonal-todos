from flask.sessions import SessionMixin
from tinydb import TinyDB
from hexagon.driven_ports.repositories import ForGettingCurrentUser, ForPersistingTodos
from hexagon.models import Todo


class TinyDbTodoRepository(ForPersistingTodos):
    def __init__(self):
        self._db = TinyDB("db.json")

    def load_all(self):
        return [Todo.from_dict(todo) for todo in self._db.all()]

    def save(self, todo):
        self._db.insert(todo.to_dict())

    def empty(self):
        self._db.truncate()


class InMemoryTodoRepo(ForPersistingTodos):
    def __init__(self):
        self._todos = []

    def save(self, todo):
        self._todos.append(todo)

    def load_all(self):
        return self._todos


class InMemoryUserRepo(ForGettingCurrentUser):
    def __init__(self):
        self.current_user = None

    def get_user(self):
        return self.current_user

    def log_in_user(self, user_name):
        self.current_user = user_name


class SessionUserRepo(ForGettingCurrentUser):
    def __init__(self, session: SessionMixin) -> None:
        self._session = session

    def get_user(self):
        return self._session.get("user_name")

    def log_in_user(self, user_name):
        self._session["user_name"] = user_name
