const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();

// eslint-disable-next-line no-unused-vars
app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

// eslint-disable-next-line no-unused-vars
app.get('/students', (req, res) => {
  countStudents(database)
    .then((output) => {
      res.status(200).send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.status(500).send(`Error: ${err.message}`);
    });
});

app.listen(1245);
module.exports = app;
