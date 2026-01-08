const http = require('http');
const app = "Hello Holberton School!"

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end(app);
});

server.listen(1245, () => {
  
});
