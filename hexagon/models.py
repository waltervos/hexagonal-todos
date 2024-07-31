class Todo:
    def __init__(self, task, user):
        self.task = task
        self.user = user

    def __eq__(self, other):
        return self.task == other.task and self.user == other.user

    def to_dict(self):
        return {"task": self.task, "user": self.user}

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["task"], dict["user"])
