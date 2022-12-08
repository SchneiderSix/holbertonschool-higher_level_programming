#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(process.argv.sort(function(a, b) { return b - a; })[1]);
}
