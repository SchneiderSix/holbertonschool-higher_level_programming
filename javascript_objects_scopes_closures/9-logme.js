#!/usr/bin/node
exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    let str = str + i;
    console.log(str + ': ' + arguments[i]);
  }
};
