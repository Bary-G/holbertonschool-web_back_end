const http = require('http');
const countStudents = require('./3-read_file_async');
const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    countStudents(database)
      .then((output) => {
        res.end(`This is the list of our students\n${output}`);
      })
      .catch((err) => {
        res.end(`Error: ${err.message}`);
      });
  }
});

app.listen(1245);
module.exports = app;
