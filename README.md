# FastAPI Project

Este é um projeto FastAPI que consome dados da API do IBGE de do TCE para fornecer informações sobre municípios do estado do Ceará.

## Pré-requisitos

- Docker: Certifique-se de ter o Docker instalado em sua máquina. [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: Certifique-se de ter o Docker Compose instalado. [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Como executar o projeto

Siga as instruções abaixo para rodar o projeto utilizando Docker:

### 1. Clone o repositório

git clone https://github.com/Joab-S/INSIGHT_TEST.git

cd seu-repositorio

### 2. Construir a imagem Docker

Execute o comando abaixo para construir a imagem Docker:

docker-compose build

### 3. Executar o container

Após a construção da imagem, execute o container com o comando:

docker-compose up

### 4. Acessar a aplicação

A aplicação estará disponível em `http://localhost:8000`.

## Documentação da API

A documentação interativa da API, gerada pelo Swagger, pode ser acessada em `http://localhost:8000/docs`.

A documentação no formato OpenAPI também está disponível em `http://localhost:8000/redoc`.
