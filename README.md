# FastAPI Project

Este é um projeto FastAPI que consome dados da API do IBGE de do TCE para fornecer informações sobre municípios do estado do Ceará.

O projeto consiste na minha proposta de solução de um case para ingresso no Insight: Data Science Lab.

Autor: Joab da Silva Rocha

LinkedIn: https://www.linkedin.com/in/joabdsr

## Pré-requisitos

- Docker: Certifique-se de ter o Docker instalado em sua máquina. [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: Certifique-se de ter o Docker Compose instalado. [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Como executar o projeto

Siga as instruções abaixo para rodar o projeto utilizando Docker:

### 1. Clone o repositório

git clone https://github.com/Joab-S/INSIGHT_TEST.git

cd INSIGHT_TEST

### 2. Construir a imagem Docker

Execute o comando abaixo para construir a imagem Docker:

docker-compose build

### 3. Executar o container

Após a construção da imagem, execute o container com o comando:

docker-compose up

nota: use a tag -d caso queira rodar o processo em segundo plano e manter o terminal livre

### 4. Acessar o terminal do container 

Caso queira, você pode acessar o terminal do Container onde o projeto está rodando.

Para isso, use o comando abaixo para acessar o terminal do container (Se seu docker não estiver rodando em segundo plano, pode ser necessário abrir outro terminal):

docker-compose exec cplex-container /bin/bash

### 5. Parando a Aplicação

No terminal onde o docker está rodando, use Ctrl + C.

Se seu container estiver rodando em segundo plano, use o comando:

docker-compose stop

Nota: Caso você queira excluir o container, então rode:

docker-compose down

### 6. Acessar a aplicação

A aplicação estará disponível em `https://infosync-municipios.onrender.com/`.

Nota: Essa rota, por sí só, apenas retorna uma lista de municípios, conforme a documentação (abaixo). Desse modo, sugiro abrir o link da documentação e ver as rotas da API por lá. 

## Documentação da API

A documentação interativa da API, gerada pelo Swagger, pode ser acessada em `http://localhost:8000/docs`.

A documentação no formato OpenAPI também está disponível em `http://localhost:8000/redoc`.
