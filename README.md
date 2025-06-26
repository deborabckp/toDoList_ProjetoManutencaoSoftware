## Definição - ToDoList

Este projeto foi desenvolvido como parte das aulas de Manutenção de Software, o objetivo era construir uma estrutura mínima funcional que permitisse a aplicação dos conceitos abordados na segunda unidade da disciplina, é uma aplicação bem simples de ToDoList ou Gerenciador de Tarefas que tem funcionalidades básicas para manipulação de tarefas, servindo como base para aprofundamento em conceitos como CRUD, modelos e views personalizados, e de controle de permissões.

## Funcionalidades Implementadas

O projeto solicita os seguintes requisitos essenciais e atende a eles:

- **Operações básicas do CRUD  (Create, Read, Update, Delete);**
- **Modelos personalizados;**
- **Serializers personalizados;**
- **Views personalizadas;**
- **UUID em modelos;**
- **Controle de permissões.**

## Como executar o projeto localmente

Siga os passos abaixo para rodar a aplicação do projeto na sua máquina:

### Pré-requisitos

- Python com versão 3.8+ instalado;
- Git instalado;
- Ambiente virtual (Abaixo tem o passo a passo do `venv`);
- Banco de dados SQLite (já está configurado por padrão no projeto).

### Passos

`1. Clone este repositório:`

```bash
git clone https://github.com/deborabckp/toDoList_ProjetoManutencaoSoftware.git
cd toDoList_ProjetoManutencaoSoftware
```
`2. Crie o ambiente virtual:`

```bash
Para linux/macOS:

python3 -m venv env
source env/bin/activate

Para windows:

python -m venv env
.\env\Scripts\Activate.ps1
```

`3. Instale as dependências:`

```bash
pip install -r requirements.txt
```

`4. Faça as migrações para criar as tabelas do banco de dados:`

```bash
python manage.py migrate
```

`5. Acesso remoto a aplicação com ngrok:`

Instale o ngrok

    sudo snap install ngrok

Faça login no site do ngrok e pegue seu token

    ngrok config add-authtoken COLE_SEU_TOKEN

Em um terminal, rode o servidor Django

    python3 manage.py runserver 8000

Em outro terminal, rode:

    ngrok http 8000

Você vai ver algo como: `Forwarding https://1234-5678-abc.ngrok-free.app -> http://localhost:8000`

Use esse link para acessar a aplicação

Login para testar:

- Usuário: `manutencao`
- Senha: `manutencao123`

### Caso queira acessar a API REST via navegador, rode novamente os comandos do passo 5, obtenha o link, a única diferença é que você deve adicionar `/api/` ao final do link.

Por exemplo. se o link for assim:

    https://seu-endereco.ngrok-free.app/

Você consegue acessar a API, assim:

    https://seu-endereco.ngrok-free.app/api/

`6. Faça Login na API:`

Você pode acessar o botão de Login no canto superior direito da página

Clique no botão e acesse com o superusuário criado para o projeto:

- Usuário: manutencao
- Senha: manutencao123

`7. Teste os endpoints:`

Após realizar login, você poderá:

- Listar tarefas (clicando em "GET")
- Criar novas tarefas (preenchendo o Title e clicando em "POST")
- Editar tarefas (através do ID usando "PUT" ou "PATCH")
- Excluir tarefas (através do ID da tarefa cadastrada e clicando em "DELETE")

## Sobre o projeto

O projeto segue a arquitetura padrão do Django, com pastas para apps, templates e arquivos de configuração, além disso, utiliza o Django REST Framework (DRF), que tem uma interface web interativa para visualizar e testar os endpoints da API.