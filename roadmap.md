# ROADMAP PYTHON

## INICIANDO NOVO PROJETO EM PYTHON

Crie um ambiente virtual:
```bash
python -m venv .venv
```

Ative o ambiente virtual:

### Linux / Mac
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
```

Instale dependências:
```bash
pip install requests
```

Gerar arquivo de dependências:
```bash
pip freeze > requirements.txt
```

Instalar dependências do projeto:
```bash
pip install -r requirements.txt
```

Estrutura inicial:
```bash
mkdir src
touch src/main.py
```

Executar o projeto:
```bash
python src/main.py
```

---

# VARIÁVEIS E TIPAGENS

```python
# Immutable
nome: str = 'Bruno'
age: int = 29
active: bool = True
fruits: tuple = ('Apple', 'Peach', 'Pineapple') # Immutable
pocket: float = 1.99
haveGold: None # None = Null or Void
gamerNumber: str | bool = 'LoL' 
gamerNumber = True

# Mutable
languages: list = [
    'Dart/Flutter',
    'Node',
    'Go'
]
register: dict[str, object] = {
    "id": "1",
    "name": "Bruno",
    "age": 29
}
sortNumbers: set = {1, 7, 14}

```

---

# CONSTANTES

Python não possui constantes reais, mas por convenção usamos MAIÚSCULAS:

```python
PI = 3.14
MAX_USERS = 100
```

---

# FUNÇÕES

```python
def sum_numbers(a: int, b: int) -> int:
    return a + b

result = sum_numbers(10, 5)

print(result)
```

Função com valor padrão:
```python
def greet(name="Bruno"):
    print(f"Olá, {name}")

greet()
```

---

# TRATAMENTO DE ERROS

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")

    return a / b

try:
    result = divide(10, 2)
    print(result)

except ValueError as error:
    print("Erro:", error)

finally:
    print("Finalizando operação")
```

---

# LISTAS

Equivalente aos slices do Go.

```python
users = []

names = [
    "Bruno",
    "José",
    "Goku"
]

names.append("Vegeta")

print(names[0])
```

Criando lista com range:
```python
numbers = list(range(5))
```

---

# FOR

```python
users = ["Bruno", "José", "Goku"]

for user in users:
    print(user)
```

Com índice:
```python
for index, user in enumerate(users):
    print(index, user)
```

---

# CLASSES E MÉTODOS

```python
class Account:
    def __init__(self, identification, holder):
        self.identification = identification
        self.holder = holder
        self.balance = 0

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Valor inválido")

        self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            raise ValueError("Saldo insuficiente")

        self.balance -= value


account = Account("1", "Bruno")

account.deposit(100)

print(account.balance)
```

---

# DICIONÁRIOS (DICT)

Equivalente ao MAP do Go.

```python
users = {
    "Bruno": 29,
    "José": 30
}

print(users["Bruno"])
```

Verificando existência:
```python
if "Bruno" in users:
    print("Usuário encontrado")
```

Percorrendo dict:
```python
for key, value in users.items():
    print(key, value)
```

---

# TUPLAS

Estrutura imutável.

```python
coordinates = (10, 20)

print(coordinates[0])
```

Desestruturação:
```python
x, y = coordinates
```


# LIST COMPREHENSION

Muito utilizado no Python.

```python
numbers = [1, 2, 3, 4]

double = [n * 2 for n in numbers]

print(double)
```

Com condição:
```python
even = [n for n in numbers if n % 2 == 0]
```

---

# FUNÇÕES LAMBDA

```python
sum_numbers = lambda a, b: a + b

print(sum_numbers(2, 3))
```

---

# DECORATORS

Permitem modificar comportamento de funções.

```python
def logger(func):
    def wrapper():
        print("Executando função...")
        func()

    return wrapper


@logger
def hello():
    print("Olá!")

hello()
```

---

# HERANÇA

```python
class Animal:
    def speak(self):
        print("Som do animal")


class Dog(Animal):
    def speak(self):
        print("Au au")


dog = Dog()

dog.speak()
```

---

# DATACLASSES

Muito utilizado para modelos simples.

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


user = User("Bruno", 29)

print(user)
```

---

# ARQUIVOS

```python
import json

# Write JSON file
def write_file() -> None:
    users = [
        {
            "name": "Bruno",
            "age": 29
        },
        {
            "name": "Goku",
            "age": 40
        },
        {
            "name": "Mel",
            "age": 54
        }
    ]

    # W -> Write
    with open("users.json", "w") as file:
        json.dump(users, file)

# Read JSON file and convert from Dict
def read_file() -> dict:
    users: dict

    # R -> Read
    with open("users.json", "r") as file:
        users = json.load(file)

    return users

# write_file()
users: dict = read_file()

print(users)    
```

---

# JSON

```python
import json

user_string: str = '{"name": "Jonas", "age": 20}'
user: dict = {
    "name": "Bruno",
    "age": 29
}

# Convert Dict from JSON
json_string: str = json.dumps(user)

# Convert JSON from Dict
json_dict: dict = json.loads(user_string)

print("JSON String: ", json_string) # '{"name": "Bruno", "age": 29}'
print("JSON Dict: ", json_dict["name"]) # Jonas

print(type(json_string)) # <class 'str'>
print(type(json_dict)) # <class 'dict'>
```

---

# REQUESTS HTTP

Biblioteca muito utilizada.

Instalação:
```bash
pip install requests
```

Uso:
```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())
```

---

# ASYNC / AWAIT

Concorrência assíncrona em Python.

```python
import asyncio


async def task():
    print("Executando tarefa...")
    await asyncio.sleep(2)
    print("Finalizada")


asyncio.run(task())
```

Múltiplas tasks:
```python
async def main():
    await asyncio.gather(
        task(),
        task()
    )

asyncio.run(main())
```

---

# CONTEXT MANAGER

Equivalente a gerenciamento automático de recursos.

```python
class Database:
    def __enter__(self):
        print("Abrindo conexão")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando conexão")


with Database():
    print("Executando operação")
```

---

# PACOTES E MÓDULOS

Estrutura sugerida:
```text
myapp/
│
├── requirements.txt
├── main.py
│
├── entities/
│   └── user.py
│
├── services/
│   └── user_service.py
│
└── repositories/
    └── user_repository.py
```

Importando módulo:
```python
from services.user_service import create_user
```

---

# VIRTUAL ENVIRONMENT

Ativar:
```bash
source venv/bin/activate
```

Desativar:
```bash
deactivate
```

---

# TESTES COM PYTEST

Instalação:
```bash
pip install pytest
```

Arquivo:
```text
test_user.py
```

Função de teste:
```python
def sum_numbers(a, b):
    return a + b


def test_sum_numbers():
    result = sum_numbers(2, 2)

    assert result == 4
```

Executar testes:
```bash
pytest
```

Modo verboso:
```bash
pytest -v
```

---

# TESTES COM EXCEPTIONS

```python
import pytest


def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")

    return a / b


def test_divide():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

# POO EM PYTHON

Encapsulamento:
```python
class User:
    def __init__(self):
        self.__password = "123456"

    def get_password(self):
        return self.__password
```

---

# THREADS

```python
import threading


def task():
    print("Executando thread")


thread = threading.Thread(target=task)

thread.start()

thread.join()
```

---

# MULTIPROCESSING

```python
from multiprocessing import Process


def task():
    print("Executando processo")


process = Process(target=task)

process.start()

process.join()
```

---

# MANIPULAÇÃO DE DATAS

```python
from datetime import datetime

now = datetime.now()

print(now)
```

Formatando:
```python
formatted = now.strftime("%d/%m/%Y")
```

---

# ENUMS

```python
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    DISABLED = "disabled"


print(Status.ACTIVE.value)
```

---

# GERADORES (YIELD)

```python
def counter():
    for i in range(5):
        yield i


for number in counter():
    print(number)
```

---

# EXCEPTIONS PERSONALIZADAS

```python
class ValidationError(Exception):
    pass


def create_user(name):
    if not name:
        raise ValidationError("Nome obrigatório")
```

---

# PIP

Instalar pacote:
```bash
pip install flask
```

Remover pacote:
```bash
pip uninstall flask
```

Listar pacotes:
```bash
pip list
```

---

# FLASK (API SIMPLES)

Instalação:
```bash
pip install flask
```

Exemplo:
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Olá mundo"}


app.run(debug=True)
```

---

# FASTAPI

Instalação:
```bash
pip install fastapi uvicorn
```

Exemplo:
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Olá mundo"}
```

Executar:
```bash
uvicorn main:app --reload
```

---

# SQLITE

```python
import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    '''
)

connection.commit()
```

---

# BOAS PRÁTICAS

- Utilize ambientes virtuais
- Utilize tipagem sempre que possível
- Evite funções gigantes
- Utilize classes apenas quando fizer sentido
- Prefira composição ao invés de herança
- Crie testes automatizados
- Utilize linters como flake8 e black
- Organize o projeto por responsabilidade
- Utilize requirements.txt ou pyproject.toml
