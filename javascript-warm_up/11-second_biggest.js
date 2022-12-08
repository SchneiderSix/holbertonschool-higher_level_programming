#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.sort();
  console.log(arr.at(-2));
}
