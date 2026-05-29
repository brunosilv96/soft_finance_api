class User:
    # Constructor
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Methods
    def greeting(self) -> None:
        print(f'Olá, meu nome é {self.name} e eu tenho {self.age} anos')

    def majority(self) -> bool:
        return self.age >= 18
    

newUser: User = User(name='Brunão', age=29)

newUser.greeting()

if(newUser.majority()):
    print("Sou maior de idade")
else:
    print("Sou menor de idade")
