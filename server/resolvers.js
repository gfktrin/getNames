const psql = require('./psqlAdapter').psql; // our adapter from psqlAdapter.js

// should match type Query in schema.js
// one function per endpoint
exports.resolvers = {
  Query: {
    alunos(_, args, ctx) {
      const alunosQuery = 'select matricula, nome from public."Alunos"';
      return psql.manyOrNone(alunosQuery);
    }
  }
};
