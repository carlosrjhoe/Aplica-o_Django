# Alura cursos online - Fundamentos Django 2: Uma aplicação web

Projeto da Alura cursos online, desenvolvido em Python3 com framework Django

## Projeto final aula 1

Nessa aula:

- Criei uma pasta para manter todo código da nossa aplicação;

- Utilizei o módulo venv, que fornece suporte para a criação de ambientes virtuais leves com meus próprios diretórios, opcionalmente isolados dos diretórios do sistema;

- Utilizei o pip para instalar o Django em meu ambiente virtual;

- Iniciei o desenvolvimento da minha aplicação com o comando django-admin start project alurareceita e subi o servidor com o comando python manage.py runserver.

## Projeto final aula 2
Nessa aula:

- Criei uma pasta templates dentro do app de receitas, para manter meus arquivos html;

- Importei uma página estilizada, com html, css e javascript;

- Carreguei esses arquivos, conhecidos como arquivos estáticos e melhoramos o visual da minha aplicação.

## Projeto final aula 3

Nessa aula:

- Ajustei os links da index, do logo através da template tag `url`;

- Criei o `base.html` para usar as mesmas partes do HTML em diferentes páginas da aplicação;

- Evitei o código duplicado do `menu` e do `footer` criando e incluindo `partials`.

## Projeto final aula 4

Nessa aula:

- Aprendi como enviar dados para o template renderizar;

- Instalei e configurei o banco de dados Postgres com a minha aplicação;

- Criei o modelo de receitas e mapiei para uma tabela no banco de dados.

## Projeto final aula 5

Nessa aula:

- Aprendi como enviar e exibir dados para uma página;

- Exibi as receitas que estão no banco de dados;

- Alterei a `url` da index, exibindo como cada receita é feita, seus ingredientes e outras informações.

## Projeto final aula 6

Nessa aula:

- Realize filtros e crie listas no seu site

- Crie e integre modelos

- Faça o admin do seu site com o Django admin

- Saiba como criar uma página de busca com páginação

## Projeto final aula 7

Nesta aula:

- Criei o app de usuários, configurei as URLs e as rotas, além de registrar o app no projeto;

- Incluí também os formulários de login, cadastro, logout e dashboard, com suas respectivas funções em views.py de usuários.

## Projeto final aula 8

Nesta aula:

- Tentei recuperar os dados do formulário através do verbo HTTP POST, porém, recebi uma mensagem informando que o token de segurança não foi encontrado;

- Para solucionar, adicionei a template tag {% csrf_token %} e recuperei o nome enviado na requisição através do código request.POST['nome'];

- Crieis algumas validações e um novo usuário na aplicação.

## Projeto final aula 9

Nesta aula:

- Busquei os dados email e senha para realizar o login do usuário, passando o token de segurança e criei a página de dashboard onde renderizei caso os campos do formulário não estejam em branco;

- Realizei o login do usuário, caso as credenciais estejam corretas exibindo o nome do usuário com o código user.username;

- Melhorei a página de dashboard e alteramos os links do menu caso o usuário esteja logado, além de criar uma forma do usuário realizar o logout.

## Projeto final aula 10

Nesta aula:

- Criei um botão capaz de deletar as receitas que criei;

- Removi o app de pessoas da aplicação e do banco de dados.

## Projeto final aula 11

Nesta aula:

- Criei o botão editar em cada receita, onde exibo o formulário da receita com as informações para editar ou alterar algum campo ou imagem;

- Após a edição, realizei a atualização da receita no banco de dados.

## Projeto final aula 12

Nesta aula:

- Refatorei a pasta de template, criando uma pasta para manter o template de cada app;

- Alterei alguns métodos da view de usuários para view de receita;

- Modularizei a view, dividindo as responsabilidades e trabalhando com mais de uma view por app.

