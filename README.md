# PROCESSO DE SELEÇÃO DE PESSOA DESENVOLVEDORA

## Informações pessoais

- Nome: Tiago de Almeida Machado Vilardi.
- Email: tiagoamx@gmail.com
- Telefone/Whatsapp: (63) 98407-1975
- Github:  [https://github.com/tiagoamx](https://github.com/tiagoamx)

## Informações do projeto

O projeto utiliza Django na Versão 4.0.*
	Usar python nas versoes compativeis: 3.8, 3.9, 3.10

Mais informações:
[https://docs.djangoproject.com/pt-br/4.0/faq/install/#what-python-version-can-i-use-with-django](https://docs.djangoproject.com/pt-br/4.0/faq/install/#what-python-version-can-i-use-with-django)

###### Instalar pacotes pip:

    `	$pip install -r requirements.tx`

Para segurança do projeto e separação de configuracões  de códigos é recomendado que se faça o seguinte passo:

    Criar o arquivo de nome` .env`  na raiz do projeto (mesmo nível do manage.py) e definir as variáveis dinâmicas conforme a seguir:

###### #Conteudo exemplo .env file

DEBUG=on

SECRET_KEY='django-my-new-secret-key'

ALLOWED_HOSTS=127.0.0.1, .localhost, .meudominio.com

#Exemplos condiguracoes de banco de dados:

#DATABASE_URL=sqlite:////full_path_to/db_local.sqlite3
#DATABASE_URL=postgresql://postgres:postgres@localhost:5432/data_base_producao

###### Executar testes no projeto:

`	pytest -v `

Executar projeto:
`	python manage.py runserver`

Acessar sistema:

    [http://localhost:8000/](http://localhost:8000/)

Acesso aos dados do banco de dados sqlite de testes:

- O usuário admin do sistema django é user:admin/senha:admin.
- O usuário aluno do sistema é user:aluno01/senha:1234567890

# Histórias desenvolvidas no projeto

- História 0:

  - BUG - a ordem das respostas da questão estão aparecendo embaralhadas para o usuário. Faça as respostas aparacerem na ordem correta para o usuário ('a', 'b', 'c', 'd' e 'e').
- História 1:

  - Crie uma estrutura de models para guardar a questão no banco de dados.
- História 2:

  - Faça com que a view pegue a questão no banco de dados.
- História 3:

  - Faça com que a view de correção use o banco de dados.
- História 4:

  - Se o sistema tiver mais de uma questão, crie um link de "próxima questão" na página de correção que leve o usuário para a próxima
    questão do banco.
  - Se a questão for a última do banco, o link "próxima questão" deve levar o usuário para a primeira questão.
- História 5: Logar cada questão respondida com:

  - data em que a questão foi respondida;
  - alternativa escolhida;
  - se a alternativa está correta ou não.

## *** BONUS ***

- História 6:

  - Crie um sistema simples de cadastro e login para o site.
  - O cadastro deve ficar na url "/cadastro/" e o login em "/login/".
  - Importante: O site deve continuar permitindo que as questões sejam respondidas por usuários deslogados. E a página raiz do site deve continuar sendo a primeira questão.
- História 7:

  - Adicione o campo "user" no log de questões feitas.
- História 8:

  - Para usuário logados, crie uma página com o log de todas as questões feitas pelo usuário em "/log-questoes/".
