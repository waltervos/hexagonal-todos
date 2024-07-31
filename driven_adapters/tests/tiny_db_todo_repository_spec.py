from driven_adapters.repositories import TinyDbTodoRepository
from hexagon.models import Todo


class DescribeTinyDbTodoRepository:
    def setup_method(self):
        self.sut = TinyDbTodoRepository()
        self.sut.empty()

    def it_can_store_a_todo_item(self):
        self.sut.save(Todo(task="Buy milk", user="Marietje Puk"))
        assert self.sut.load_all() == [Todo(task="Buy milk", user="Marietje Puk")]

    def it_can_store_multiple_todo_items(self):
        self.sut.save(Todo(task="Buy milk", user="Marietje Puk"))
        self.sut.save(Todo(task="Buy soy milk", user="Marietje Puk"))
        assert self.sut.load_all() == [
            Todo(task="Buy milk", user="Marietje Puk"),
            Todo(task="Buy soy milk", user="Marietje Puk"),
        ]
