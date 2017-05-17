.. _llabs_doc:

#####################################
``LLabs`` - Desafio Backend luizalabs
#####################################


.. topic:: Descrição

     API desenvolvida em python para coletar informações de usuários do facebook, armazenar em um banco de dados, fornecer um serviço de acesso e fazer logging das ações.

     A aplicação foi hospedada no `Heroku <http://www.heroku.com>`_ . `Clique aqui <https://sdnlabs.herokuapp.com>`_ para testa-la.


    :Data: **17/05/2017**
    :Autor: **Sidon Duarte**


Informações coletadas e armazenadas:
************************************

- Facebook ID
- Nome
- Gênero
- Email


.. sidebar:: Observação:
    :subtitle: Campo obsoleto na API do Facebook.

      Originalmente o desafio solicita o campo *Username ao* invés do *email*, mas a documentação da API do facebook informa que esse campo está obsoleto a partir da versão 2.x da api.


Opções com o comando curl:
***********************************

Raiz da API:
============
::

    $ curl https://sdnlabs.herokuapp.com/
    {"persons":"https://sdnlabs.herokuapp.com/persons/",
    "logging":"https://sdnlabs.herokuapp.com/logging/"}


Inserir usuários do facebook ao banco de dados:
===============================================
::

    $ curl --user user:senha --data "facebookId=4" https://sdnlabs.herokuapp.com/persons/
    {"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://sdnlabs.herokuapp.com/persons/4/"}}

    $ curl --user user:senha --data "facebookId=1299" https://sdnlabs.herokuapp.com/persons/
    {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://sdnlabs.herokuapp.com/persons/1299/"}}

    $ curl --user user:senha --data "facebookId=1399" https://sdnlabs.herokuapp.com/persons/
    {"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook",
     "links": {"self":"https://sdnlabs.herokuapp.com/persons/1399/"}}

Listar todos os usuarios:
=========================
::

    $ curl --user user:senha https://sdnlabs.herokuapp.com/persons/
    [{"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
      "links": {"self":"https://sdnlabs.herokuapp.com/persons/4/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://sdnlabs.herokuapp.com/persons/1299/"}},
     {"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook",
      "links": {"self":"https://sdnlabs.herokuapp.com/persons/1399/"}}]

Listar somente os dois primeiros usuários:
==========================================
::

    $ curl --user user:senha https://sdnlabs.herokuapp.com/persons/?limit=2
    [{"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://sdnlabs.herokuapp.com/persons/4/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://sdnlabs.herokuapp.com/persons/1299/"}}]


Listar os dois últimos usuários:
==========================================
::

    $ curl --user user:senha https://sdnlabs.herokuapp.com/persons/?last=2
    [{"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook","links":
     {"self":"https://sdnlabs.herokuapp.com/persons/1399/"}},
     {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
      "links":{"self":"https://sdnlabs.herokuapp.com/persons/1299/"}}]

Excluir um usuário:
====================
::

    curl --user user:senha -X DELETE https://sdnlabs.herokuapp.com/persons/1399/

Exibir as informações de um usuário:
====================================
::

    $ curl --user user:senha https://sdnlabs.herokuapp.com/persons/1399/
    {"detail":"Não encontrado."}

    $ curl --user user:senha https://sdnlabs.herokuapp.com/persons/4/
    {"facebookId":4,"name":"Mark Zuckerberg","gender":"Not in facebook","email":"Not in facebook",
     "links":{"self":"https://sdnlabs.herokuapp.com/persons/4/"}}

Exibir os logs de acessos:
==========================
::

    $ curl --user user:senha https://sdnlabs.herokuapp.com/logging/
    {"user":null,"requested_at":"2017-05-16T18:02:49.236681Z","path":"/persons/","remote_addr":"127.0.0.1","host":"127.0.0.1:8007","method":"GET","query_params":"{}","data":null,"response":"\n\n\n\n<!DOCTYPE html>\n<html>\n  <head>\n    \n\n      \n        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>\n        <meta name=\"robots\" content=\"NONE,NOARCHIVE\" />\n      \n\n      <title>Person List – Django REST framework</title>\n\n      \n        \n          <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/bootstrap.min.css\"/>\n          <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/bootstrap-tweaks.css\"/>\n        \n\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/prettify.css\"/>\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/rest_framework/css/default.css\"/>\n      \n\n    \n  </head>\n\n  \n  <body class=\"\">\n\n    <div class=\"wrapper\">\n      \n        <div class=\"navbar navbar-static-top navbar-inverse\">\n          <div class=\"container\">\n            <span>\n              \n                <a class='navbar-brand' rel=\"nofollow\" href='http://www.django-rest-framewor
    ...

Acesso a API via browser:
*************************

.. topic:: Hospedado no Heroku, token válido por 2 meses.

    :Raiz: https://sdnlabs.herokuapp.com/
    :Usuários: https://sdnlabs.herokuapp.com/persons/
    :Tracking: https://sdnlabs.herokuapp.com/logging/


Instalação e execução local
***************************

Para execução local, descompactar o arquivo llabs/config/llabs.conf.zip que contem um arquivo do tipo json (llabs.json) com o token para acesso a API do facebook e parte da configuração do arquivo llabs/settings.py.

