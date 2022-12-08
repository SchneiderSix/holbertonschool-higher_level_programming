#!/usr/bin/node
const process = require('process');
function factorialize (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
if (isNaN(process.argv[2])) {
  console.log('1');
} else {
  console.log(factorialize(process.argv[2]));
}
