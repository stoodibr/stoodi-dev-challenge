# PROCESSO DE SELEÇÃO DE PESSOA DESENVOLVEDORA
- Artur Felipe da Silva Veloso
- arturfdasveloso@gmail.com
- (86) 99927-2370
- Teresina/PI

## Considerações:
- Se não for possível fazer todas as histórias, entregue apenas as histórias que você fez.
- Você será avaliado tanto pelas funcionalidade do seu código quanto pela utilização de boas práticas, desenvolva como se fosse um código de produção em um time e não uma prova ou script.
- Neste teste vamos focar apenas nas funcionalidades. A apresentação do site não contará pontos.
- O usuário admin do sistema django é user:admin/senha:admin.
- Se você usa docker, basta rodar `make build && make up` para ter o projeto rodando em http://localhost:8000/
- Não se esqueça de fazer testes unitários!!


# Histórias

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

