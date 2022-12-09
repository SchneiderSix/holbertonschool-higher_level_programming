#!/usr/bin/node
exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    const n = 0;
    console.log(n + ': ' + arguments[i]);
    n += 1;
  }
};
