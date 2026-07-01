# Tasks Flask CRUD

> API REST simples para gerenciamento de tarefas (To-Do), construída com Flask puro como exercício da Formação Python da Rocketseat

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.3-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)

---

## 📋 Sobre o projeto

**Tasks Flask CRUD** é uma API REST para gerenciamento de tarefas, desenvolvida como projeto de estudo dentro da Formação em Python da Rocketseat. O objetivo é praticar os fundamentos da construção de uma API CRUD (Create, Read, Update, Delete) usando Flask puro, sem framework de ORM, trabalhando com rotas, manipulação de JSON e testes automatizados de integração.

As tarefas são armazenadas em memória durante a execução da aplicação (sem banco de dados), o que torna o projeto leve e ideal para fins didáticos.

### Principais características

- ✅ **CRUD completo** — criação, listagem, consulta, atualização e remoção de tarefas
- ✅ **API RESTful** com respostas em JSON
- ✅ **Modelo de dados dedicado** (`Task`) separado da camada de rotas
- ✅ **Testes automatizados** com `pytest` + `requests`, validando os endpoints de ponta a ponta
- ✅ **Código simples e didático**, sem dependências externas de banco de dados

---

## 🏗️ Arquitetura

### Stack utilizada

- **Linguagem**: Python 3.10+
- **Framework Web**: Flask 2.3.0
- **Testes**: Pytest 7.4.3 + Requests 2.31.0

### Estrutura do projeto

```
tasks-flask-crud/
├── models/
│   └── task.py        # Classe Task (modelo dos dados da tarefa)
├── app.py              # Aplicação Flask e definição das rotas
├── tests.py             # Testes de integração da API
├── requirements.txt      # Dependências do projeto
└── .gitignore
```

### Modelo de dados

Cada tarefa (`Task`) possui os seguintes atributos:

| Campo         | Tipo    | Descrição                          |
|---------------|---------|-------------------------------------|
| `id`          | int     | Identificador único da tarefa       |
| `title`       | string  | Título da tarefa                    |
| `description` | string  | Descrição da tarefa                 |
| `completed`   | boolean | Indica se a tarefa foi concluída    |

> ⚠️ As tarefas são mantidas em uma lista em memória (`tasks = []`), portanto os dados são perdidos a cada reinicialização da aplicação.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/igorland1/tasks-flask-crud.git
cd tasks-flask-crud
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Execute a aplicação**

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`, em modo debug.

---

## 📡 Endpoints da API

### Visão geral

```http
POST    /tasks             # Cria uma nova tarefa
GET     /tasks             # Lista todas as tarefas
GET     /tasks/<id>        # Busca uma tarefa específica pelo ID
PUT     /tasks/<id>        # Atualiza uma tarefa existente
DELETE  /tasks/<id>        # Remove uma tarefa
```

### Exemplos de requisições

**Criar tarefa**

```http
POST /tasks
Content-Type: application/json

{
  "title": "Estudar Flask",
  "description": "Revisar rotas e métodos HTTP"
}
```

Resposta:

```json
{
  "message": "Nova tarefa criada com sucesso",
  "id": 1
}
```

**Listar tarefas**

```http
GET /tasks
```

Resposta:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Flask",
      "description": "Revisar rotas e métodos HTTP",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

**Buscar tarefa por ID**

```http
GET /tasks/1
```

**Atualizar tarefa**

```http
PUT /tasks/1
Content-Type: application/json

{
  "title": "Estudar Flask e SQLAlchemy",
  "description": "Revisar rotas, métodos HTTP e ORM",
  "completed": true
}
```

Resposta:

```json
{
  "message": "Tarefa atualizada com sucesso"
}
```

**Remover tarefa**

```http
DELETE /tasks/1
```

Resposta:

```json
{
  "message": "Tarefa deletada com sucesso"
}
```

**Erro — tarefa não encontrada**

```json
{
  "message": "Task não encontrada."
}
```
Status: `404 Not Found`

---

## 🧪 Testes

O projeto conta com testes de integração que validam o fluxo completo do CRUD (criar → listar → buscar → atualizar → deletar).

> Os testes fazem requisições HTTP reais contra a aplicação, então é necessário que o servidor Flask esteja rodando antes de executá-los.

**1. Inicie a aplicação em um terminal**

```bash
python app.py
```

**2. Em outro terminal, rode os testes**

```bash
pytest tests.py
```

---

## 🎯 Aprendizados demonstrados neste projeto

- Criação de rotas RESTful com Flask (`GET`, `POST`, `PUT`, `DELETE`)
- Manipulação de requisições e respostas em JSON
- Separação entre modelo de dados e camada de rotas
- Uso de códigos de status HTTP para representar sucesso e erro
- Escrita de testes de integração com `pytest` e `requests`

---

## 🔜 Possíveis evoluções

- Persistência dos dados com banco de dados (SQLite/PostgreSQL) via SQLAlchemy
- Documentação interativa da API (Swagger/OpenAPI)

---

## 📝 Licença

Projeto de estudo, disponibilizado como código aberto para fins de aprendizado e portfólio.

---

## 🤝 Contato

Projeto desenvolvido por [Igor](https://github.com/igorland1) como parte da Formação em Python da Rocketseat.