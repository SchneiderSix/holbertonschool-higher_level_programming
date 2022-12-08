#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (const i in process.argv) {
    let fir = 0;
    let sec = 0;
    if (i > fir) {
      sec = fir;
      fir = i;
    }
  console.log(sec);
  }
}
