#!/usr/bin/node
const fs = require('fs');
let data = process.argv[3];
fs.readFile(process.argv[2], 'utf8', data, (err) => {
  if (err) {
    console.error(err);
  };
});
