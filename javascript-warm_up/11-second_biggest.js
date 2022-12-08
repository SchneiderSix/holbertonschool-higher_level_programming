#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv;
  const sort_arr = [];
  for (const i in arr) {
    sort_arr.push(i);
  }
  const res = sort_arr[arr.length - 2];
  console.log(res);
}
