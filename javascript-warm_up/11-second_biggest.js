#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.sort(function(a, b){return a - b});
  const res = arr[arr.length - 2];
  console.log(res);
}
