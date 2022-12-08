#!/usr/bin/node
const process = require('process');
if (Number.isInteger(process.argv[2])) {
  console.log('My number is: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
