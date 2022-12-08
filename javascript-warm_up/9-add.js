#!/usr/bin/node
const process = require('process');
function add(a, b) {
    return a + b;
}
if ((process.argv[2]) && (process.argv[3])) {
  console.log(add(process.argv[2], process.argv[3]));
} else {
  console.log('NaN');
}
