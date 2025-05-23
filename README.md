# 📚 API de Gerenciamento de Livros

API RESTful simples construída com Flask para cadastrar, editar, listar e remover livros. Ideal para fins didáticos ou para projetos iniciais em Python com Flask.

## 🚀 Funcionalidades

- ✅ Listar todos os livros
- 📘 Consultar livro por ID
- ➕ Cadastrar novo livro
- ✏️ Atualizar dados de um livro
- ❌ Remover livro por ID

---

## 📦 Estrutura de Diretórios
.

├── app.py # Fábrica da aplicação Flask

├── run.py # Inicializador da aplicação

├── models/ # Simulação de banco de dados (lista em memória)

├── services/ # Lógica de negócio

├── routes/ # Rotas da API

├── utils/ # Funções auxiliares (respostas JSON)

└── tests/ # Testes unitários (pytest)


---

## ▶️ Como executar

### Ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### Instalação de dependências
```
pip install -r requirements.txt

```
### Execução do servidor
```
python run.py

```
### Testes
```
pytest --cov=.

````

## 📌 Endpoints

| Método | Rota           | Descrição                  |
| ------ | -------------- | -------------------------- |
| GET    | `/livros`      | Lista todos os livros      |
| GET    | `/livros/<id>` | Consulta um livro por ID   |
| POST   | `/livros`      | Cadastra um novo livro     |
| PUT    | `/livros/<id>` | Edita os dados de um livro |
| DELETE | `/livros/<id>` | Remove um livro            |

## ⚠️ Observações
- Os dados são armazenados em memória (models/livro.py).
- Criado para estudo, testes ou demonstrações, não em produção.



