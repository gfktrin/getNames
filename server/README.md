# Overview
Uma API graphql simples para disponibilizar nome e matricula dos alunos de BSI da UNIRIO.

# Contributing

TODO

# How to run
Primeiro, crie um banco de dados postgresql e importe os dados para o banco, configure no `psqlAdapter.js`, o banco deve possuir uma tabela `Alunos` com colunas: matricula - bigint(not null e primary key) e nome - text(not null).

- Install [node](https://nodejs.org/en/)
- Install [yarn](https://yarnpkg.com/)
- Run `yarn install` in the folder.
- Run `yarn start`
- Open http://localhost:3000/graphiql to view it in the browser with graphiql.

# Example queries
```
query {
  alunos {
    matricula
    nome
  }
}
```
