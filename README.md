To-Do List API
Uma API simples para gerenciamento de tarefas, desenvolvida com Flask e SQLAlchemy.



Funcionalidades
Listar todas as tarefas (GET)
Visualizar uma tarefa específica (GET)
Criar uma nova tarefa (POST)
Atualizar uma tarefa (PUT)
Deletar uma tarefa (DELETE)

Como executar o projeto
Pré-requisitos:
Python 3.x instalado
Biblioteca Flask e SQLAlchemy

Instale as dependências:
pip install -r requirements.txt

Execute o servidor:
python app.py
O servidor será executado em http://127.0.0.1:5000

 Endpoints
1. Listar todas as tarefas
URL: /tasks
Método: GET
Descrição: Retorna uma lista com todas as tarefas.

2. Criar uma nova tarefa
URL: /tasks
Método: POST
Descrição: Cria uma nova tarefa no banco de dados.

3. Obter uma tarefa específica
URL: /tasks/<task_id>
Método: GET
Descrição: Retorna uma tarefa específica com base no ID.
Parâmetros:
task_id (int): ID da tarefa.

4. Atualizar uma tarefa
URL: /tasks/<task_id>
Método: PUT
Descrição: Atualiza o título e o status de uma tarefa.
Parâmetros:
task_id (int): ID da tarefa.

5. Deletar uma tarefa
URL: /tasks/<task_id>
Método: DELETE
Descrição: Remove uma tarefa do banco de dados.
Parâmetros:
task_id (int): ID da tarefa.



Estrutura do Projeto:
to-do-list-api/
│
├── app.py                  # Inicialização da aplicação Flask
├── requirements.txt        # Dependências do projeto
├── app/
│   ├── __init__.py         # Inicialização do módulo
│   ├── database.py         # Configuração do banco de dados
│   ├── models.py           # Modelos do banco de dados
│   └── routes.py           # Rotas da API


Testando a API
Você pode testar os endpoints usando Postman.

Banco de Dados
O banco de dados utilizado é o SQLite. O arquivo do banco será gerado automaticamente na pasta do projeto.

