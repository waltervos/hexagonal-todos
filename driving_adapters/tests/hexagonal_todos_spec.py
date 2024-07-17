from driven_adapters.repositories import InMemoryTodoRepo, InMemoryUserRepo
from hexagon import HexagonalTodos


class DescribeHexagonalTodos:
    def it_should_not_show_any_todos_if_none_have_been_added(self):
        sut = HexagonalTodos(todo_repo=InMemoryTodoRepo(), user_repo=InMemoryUserRepo())
        assert sut.view_todos() == []

    def it_should_show_todos_that_have_been_added(self):
        sut = HexagonalTodos(todo_repo=InMemoryTodoRepo(), user_repo=InMemoryUserRepo())
        sut.add_todo("Buy milk")
        assert sut.view_todos()[0].task == "Buy milk"

    def it_should_show_todos_for_the_logged_in_user_only(self):
        user_repo = InMemoryUserRepo()
        sut = HexagonalTodos(todo_repo=InMemoryTodoRepo(), user_repo=user_repo)
        
        user_repo.log_in_user("Marietje Puk")
        sut.add_todo("Buy soy milk")
        
        user_repo.log_in_user("Pietje Puk")
        sut.add_todo("Buy milk")
        result = sut.view_todos()
        
        assert len(result) == 1
        assert result[0].task == "Buy milk"


