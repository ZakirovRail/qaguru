from dataclasses import dataclass
from enum import Enum


class UserStatus(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    name: str
    age: int
    status: UserStatus
    items: list[str]

    def is_adult(self):
        return self.age > 18

    def get_items_length(self):
        return len(self.items)

    @classmethod
    def from_csv_user(cls, user: dict):
        return cls(name=user["name"],
                   age=int(user["age"]),
                   status=UserStatus(user["status"]),
                   items=user["items"].split(","))


def get_user_from_csv(user: dict):
    return User(name=user["name"],
                age=int(user["age"]),
                status=UserStatus(user["status"]),
                items=user["items"].split(","))


class Worker(User):
    status = UserStatus.worker

    def do_work(self):
        print("Im working!")

    @classmethod
    def from_user(cls, user: User):
        assert user.status == cls.status, "Воркера можно создать только из пользователя со статусом worker"
        return cls(name=user.name, age=user.age, status=cls.status, items=user.items)

    @classmethod
    def from_csv_user(cls, user: dict):
        raise NotImplementedError


if __name__ == '__main__':
    vasily = User("Vasily", 18, "worker", items=["book", "pen"])
    anna = User("Anna", 17, "student", ["laptop"])

    assert vasily.get_items_length() == 2
    assert anna.get_items_length() == 1

    User.get_items_length(vasily)

    w = Worker.from_user(vasily)
    print()
