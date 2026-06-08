# BS Aesthetics API

Backend em Python para um sistema de agendamento, construído com **FastAPI** seguindo uma organização em **MVC**.

Este projeto representa a camada de API para atender o domínio de:
- Clientes
- Serviços
- Agenda de horários
- Base para evolução de produtos e relatórios

## Objetivo do Projeto

Centralizar e organizar as operações do negócio que hoje são feitas manualmente (ex.: via WhatsApp), oferecendo uma API estruturada para:
- Cadastro e gestão de clientes
- Suporte a agendamentos e histórico
- Evolução para gestão de serviços, produtos e relatórios

## Escopo Funcional (baseado no discovery/scope)

### Versão 1.0.0
- Cadastro de clientes
- Login (cadastro próprio ou rede social)
- Visualização de serviços e preços
- Agendamento com regras de antecedência
- Histórico de agendamentos (remarcar/cancelar)
- Gerenciamento de agenda
- Relatório simples do dia

### Versão 2.0.0
- Visualização de produtos (preço e estoque)
- Contato sobre produtos via WhatsApp
- Gerenciamento de produtos
- Disparo de notificações
- Relatórios detalhados

## Arquitetura

A API segue separação por camadas no estilo MVC:

- **Models**: estruturas de domínio
- **Views/Controllers**: entrada HTTP e orquestração de casos de uso
- **Schemas**: contratos de entrada/saída
- **Repositories**: persistência
- **Routers**: definição de rotas
- **Errors**: tratamento centralizado de erros

## Stack

- Python
- FastAPI
- Uvicorn (servidor ASGI)

## Estrutura do Projeto

```text
src/
  app.py
  dependencies.py
  controllers/
  errors/
  models/
  repositories/
  routers/
  schemas/
tests/
requirements.txt
pyproject.toml
```

## Execução Local

### 1. Criar e ativar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Subir a API

```bash
fastapi dev
```

API disponível em:
- `http://localhost:8000`
- Documentação Swagger: `http://localhost:8000/docs`

## Docker

Apenas o backend será dockerizado.

### Build da imagem

```bash
docker build -t bs-aesthetics-api .
```

### Execução do container

```bash
docker run --rm -p 8000:8000 bs-aesthetics-api
```

## Testes

Com o ambiente virtual ativo:

```bash
pytest
```
