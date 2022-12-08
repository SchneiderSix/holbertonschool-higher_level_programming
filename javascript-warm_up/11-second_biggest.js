#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(1);
} else {
  for (const i in process.argv) {
    let res = 0;
    if (i > res) {
      res = i;
    }
  }
}
