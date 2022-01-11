import dataclasses

# standard inheritance
from abc import ABC, abstractmethod


class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    def __str__(self):
        return f"{self.name} of {self.surname}"


data = ("Gabriel", "Starczewski")
admin = Admin(*data)
print(admin)


# with dataclasses
class AbstractPlayer(ABC):
    @abstractmethod
    def present(self) -> str:
        pass


@dataclasses.dataclass
class Player:
    number: int

    def present(self):
        return self.number


@dataclasses.dataclass
class FootballPlayer(Player):
    position: str

    def present(self):
        return str(self.number) + " " + self.position


ronaldo = FootballPlayer(9, "attacker")
print(ronaldo.present())
