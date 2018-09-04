const GraphQLSchema = require('graphql').GraphQLSchema;
const makeExecutableSchema = require('graphql-tools').makeExecutableSchema;

const resolvers = require('./resolvers').resolvers; // our resolver from resolver.js

// define our user type
// then define a users query, which must return an array type that optionally contains 0 or more User types
const typeDefs = `
  type Aluno {
    matricula: String
    nome: String
  }

  type Query {
    alunos: [Aluno]!
  }
`;

exports.schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});
