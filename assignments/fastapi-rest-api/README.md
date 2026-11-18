# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para um catálogo de livros usando FastAPI e modelos Pydantic. Você praticará rotas HTTP, validação de dados, operações CRUD e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Consultar livros

#### Descrição
Instale FastAPI e Uvicorn com `python -m pip install fastapi uvicorn` e implemente os endpoints de consulta no arquivo `starter-code.py`. Execute a aplicação com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI que possa ser iniciada pelo comando fornecido.
- Implementar `GET /books` para retornar todos os livros cadastrados como JSON.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID.
- Retornar o status HTTP `404` quando o ID solicitado não existir.
- Disponibilizar a documentação interativa da API em `/docs`.

### 🛠️ Cadastrar livros

#### Descrição
Implemente a criação de livros. Use o modelo Pydantic fornecido para validar os dados enviados no corpo da requisição e atribua um ID ao novo livro.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para cadastrar um livro com título, autor e ano.
- Retornar o livro criado, incluindo seu ID, com status HTTP `201`.
- Rejeitar dados inválidos, como título ou autor vazio e ano menor ou igual a zero, usando a validação do modelo.
- Manter os livros em memória enquanto a aplicação estiver em execução.

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações de atualização e exclusão para que os clientes possam manter o catálogo usando o ID de cada livro.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e retornar uma confirmação.
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro que não existe.
- Permitir testar os endpoints e visualizar suas respostas pela documentação em `/docs`.