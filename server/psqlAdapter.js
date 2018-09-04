const pgPromise = require('pg-promise');

const connStr = 'postgresql://localhost:5432/testapp'; // add your psql details

const pgp = pgPromise({}); // empty pgPromise instance
const psql = pgp(connStr); // get connection to your db instance

exports.psql = psql;
