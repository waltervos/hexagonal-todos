import datetime
from driven_adapters.repositories import InMemoryTodoRepo, InMemoryUserRepo
from driven_adapters.recipients import InMemoryDeadlineAlertRecipient

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


class DescribeDeadlines:
    def it_should_not_notify_the_user_if_there_are_no_todos_due_today(self):
        recipient = InMemoryDeadlineAlertRecipient()
        sut = HexagonalTodos(todo_repo=InMemoryTodoRepo(), user_repo=InMemoryUserRepo())
        sut.notify_for_deadlines()
        assert recipient.received_alerts == []

    def it_should_notify_the_user_when_there_is_one_due_todo_today(self):
        user_repo = InMemoryUserRepo()
        recipient = InMemoryDeadlineAlertRecipient()
        sut = HexagonalTodos(
            todo_repo=InMemoryTodoRepo(), user_repo=user_repo, recipient=recipient
        )

        user_repo.log_in_user("Pietje Puk")
        sut.add_todo("Buy milk", datetime.date(2024, 7, 31))

        sut.notify_for_deadlines(date=datetime.date(2024, 7, 31))

        assert recipient.received_alerts_by_user["Pietje Puk"] == ["Buy milk"]
