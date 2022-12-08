#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  arr = [process.argv.sort()];
  console.log(arr.reverse()[1]);
}
