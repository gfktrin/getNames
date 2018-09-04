# Overview
Uma API graphql simples para disponibilizar nome e matricula dos alunos de BSI da UNIRIO.

# Contributing

TODO

# How to run
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
