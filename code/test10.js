// test/vuln-sql-node.js
const mysql = require('mysql');
const http = require('http');

const con = mysql.createConnection({ host: 'db', user: 'app', password: 'secret', database: 'appdb' });

http.createServer((req, res) => {
  const name = new URL(req.url, `http://${req.headers.host}`).searchParams.get('name') || '';
  // Vulnerable: concatenated SQL string with untrusted input
  const q = `SELECT * FROM users WHERE name = '${name}'`;
  con.query(q, (err, rows) => {
    if (err) return res.end('error');
    res.end(JSON.stringify(rows));
  });
}).listen(8080);
