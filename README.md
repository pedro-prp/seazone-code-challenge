<h1 align="center"> Seazone Code Challenge </h1>

<p align="center">
  <img src="./doc/assets/seazone-logo.png" alt="Logo Seazone" style="width: 70%; display: block; margin: 0 auto;">
  <br>
</p>


<p align="center">
  <a href="#📋-sobre">📋 Sobre</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#🚀-tecnologias">🚀 Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#⚙-como-rodar">⚙ Como Rodar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#🌐-endpoints">🌐 Endpoints</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#📝-license">📝 License</a>
</p>

## 📋 Sobre

Este desafio consiste na criação de três APIs REST utilizando Python, Django e Django Rest Framework para a empresa fictícia Khanto. O objetivo é desenvolver um sistema de gerenciamento de imóveis, anúncios e reservas.


## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Swagger](https://swagger.io/)

## ⚙ Como Rodar

### 1. Dependências

Primeiramente, você vai precisar ter o [Docker]((https://www.docker.com/)) e o [docker-compose](https://docs.docker.com/compose/install/) instalados na sua máquina.

### 2. Baixando Repositório

```bash
$ git clone git@github.com:pedro-prp/seazone-code-challenge.git

$ cd seazone-code-challenge
```

### 3. Iniciando a aplicação

Para configurar as variáveis de ambiente, basta rodar o comando:
```bash
cp .env.example .env
```


E para iniciar a aplicação, basta rodar o seguinte comando:

```bash
$ docker-compose up
```

O próprio docker-compose vai se encarregar de criar o banco de dados, rodar as migrações e iniciar o servidor.
Além disso, o docker-compose vai criar um usuário admin com as seguintes credenciais:
```bash
    username: admin
    password: admin
```

E ainda vai carregar alguns dados iniciais para a aplicação. Tudo isso ocorre devido ao arquivo de entrypoint `django.sh` que é executado quando o container é iniciado.

### 4. Acessando a aplicação

Com a aplicação rodando, você tem acesso aos seguintes links:

| Nome           | Link                             | Descrição |
|----------------|----------------------------------|-----------|
| API Swagger    | http://localhost:8000/swagger/   | O Swagger é uma estrutura para projetar, criar e documentar APIs de forma eficiente, usando o formato JSON ou YAML. Ele simplifica o desenvolvimento e o consumo de APIs, fornecendo documentação interativa e a capacidade de gerar clientes SDK em várias linguagens de programação. |
| Admin          | http://localhost:8000/admin/     | O Django admin é uma interface de administração pronta e personalizável do Django para gerenciar dados do aplicativo sem escrever código adicional.  |
| Redoc          | http://localhost:8000/redoc/     | O Redoc é uma ferramenta que gera documentação interativa para APIs com base na especificação OpenAPI, facilitando a compreensão e integração com a API. |

## 🌐 Endpoints

A aplicação possui os seguintes endpoints:


### 1. API de Properties
| Método | Endpoint          | Descrição                           |
|--------|-------------------|-------------------------------------|
| GET    | /properties/      | Lista todas as propriedades         |
| POST   | /properties/      | Cria uma nova propriedade           |
| GET    | /properties/{id}/ | Retorna uma propriedade específica  |
| PUT    | /properties/{id}/ | Atualiza uma propriedade específica |
| DELETE | /properties/{id}/ | Deleta uma propriedade específica   |


### 2. API de Advertisements
| Método  | Endpoint              | Descrição                           |
|---------|-----------------------|-------------------------------------|
| GET    | /advertisements/      | Lista todos os anúncios             |
| POST   | /advertisements/      | Cria um novo anúncio                 |
| GET    | /advertisements/{id}/ | Retorna um anúncio específico  |
| PUT    | /advertisements/{id}/ | Atualiza um anúncio específico |


### 3. API de Bookings
| Método | Endpoint        | Descrição |
|--------|-----------------|-----------|
| GET | /bookings/      | Lista todas as reservas |
| POST | /bookings/      | Cria uma nova reserva |
| GET | /bookings/{id}/ | Retorna uma reserva específica |
| DELETE | /bookings/{id}/ | Deleta uma reserva específica |

## 📝 License

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.