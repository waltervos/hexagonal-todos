from flask import Flask, redirect, render_template, request, session

from driven_adapters.repositories import (
    TinyDbTodoRepository,
    InMemoryUserRepo,
    SessionUserRepo,
)
from hexagon import HexagonalTodos

app = Flask(__name__)
app.secret_key = "super secret"

user_repo = SessionUserRepo(session=session)
hexagonal_todos = HexagonalTodos(todo_repo=TinyDbTodoRepository(), user_repo=user_repo)


@app.route("/")
def hello():
    return render_template("index.html", todos=hexagonal_todos.view_todos())


if __name__ == "__main__":
    app.run()


@app.post("/add-todo")
def add_todo():
    hexagonal_todos.add_todo(request.form["todo"])
    return redirect("/")


@app.get("/login")
def login_form():
    return render_template("login.html")


@app.post("/login")
def login():
    user_repo.log_in_user(request.form["user_name"])
    return redirect("/")
