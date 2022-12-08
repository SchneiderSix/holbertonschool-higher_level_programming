#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let arr = process.argv.sort();
  arr.reverse();
  console.log(arr[1]);
}
