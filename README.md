# PROCESSO DE SELEÇÃO DE ENGENHEIRO DE SOFTWARE

Este repositório faz parte da primeira fase do processo seletivo do Stoodi.

Se você não tem experiência com o Django, recomendamos que você faça pelo menos
este tutorial antes de começar:
https://docs.djangoproject.com/en/1.11/intro/tutorial01/

Neste repositório, encontra-se o código de um sistema simples desenvolvido em
Django(1.11.x). O sistema consiste em uma página que contém uma questão de
múltipla escolha, ao respondê-la o usuário recebe um feedback de acerto ou erro.


## Para participar desta parte do processo você deve:
1. Fazer um fork deste projeto;
2. Criar um repositório FECHADO(private) na sua conta do bitbucket;
3. Colocar o seu nome email e nome no topo deste arquivo README do seu
   repositório;
4. Desenvolver as histórias pedidas abaixo no seu repositório. De preferência,
   com pelo menos um commit na finalização de cada história;
5. Ao terminar o desenvolvimento, dê acesso de leitura ao usuário
   bgfranca(brunogomesfranca@gmail.com) ao seu repositório.


## Considerações:
- Se não for possível fazer todas as histórias, entregue apenas as histórias que você fez.
- Você será avaliado tanto pelas funcionalidade do seu código quanto pela utilização de boas práticas, desenvolva como se fosse um código de produção em um time e não uma prova ou script.
- Cuidado para não deixar o seu repositório público!
- Neste teste vamos focar apenas nas funcionalidades. A apresentação do site não contará pontos.
- O usuário admin do sistema django é user:admin/senha:admin.
- Se você usa docker, basta rodar `make build && make up` para ter o projeto rodando em http://localhost:8000/


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

