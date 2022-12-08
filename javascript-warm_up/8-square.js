#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2]) > 0) {
  for (let i = 0; i < process.argv[2]; i++) {
    let row = ''
    for (let j = 0; j < process.argv[2]; j++) {
      row += 'X'
    }
    console.log(row)
  }
} else {
  console.log('Missing size');
}
