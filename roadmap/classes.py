from dataclasses import dataclass


# Create automatically init, repr and eq (DTO and Entities)
@dataclass
class Customer:
    id: str
    name: str
    email: str


# Traditional class (general purpose)
class User:
    # Constructor
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Methods
    def greeting(self) -> None:
        print(f"Olá, meu nome é {self.name} e eu tenho {self.age} anos")

    def majority(self) -> bool:
        return self.age >= 18

    # Factory Method - Return a instance of User
    @classmethod
    def empty(cls) -> User:
        return cls("", 0)

    # Static Method - Without access to class (cls) or object (self)
    @staticmethod
    def random() -> None:
        print("Alguma coisa aleatória")


newUser: User = User(name="Brunão", age=29)
emptyUser: User = User.empty()

emptyUser.random()

newUser.greeting()

if newUser.majority():
    print("Sou maior de idade")
else:
    print("Sou menor de idade")
