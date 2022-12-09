#!/usr/bin/node
exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    let k = 0;
    console.log(k + ": " + arguments[i]);
    k += 1;
  }
};
