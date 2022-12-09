#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (c === null) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += C;
        }
        console.log(row);
      }
    }
  }
};
