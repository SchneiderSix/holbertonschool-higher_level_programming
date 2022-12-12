#!/usr/bin/node
const fs = require('fs');

/* Read File */
fs.readFile(arguments[0], bar)

function bar (err, data) {
  err ? console.log({err}) : console.log(JSON.stringify(data));
};
