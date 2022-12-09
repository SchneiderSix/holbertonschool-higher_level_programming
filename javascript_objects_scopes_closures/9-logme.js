#!/usr/bin/node
exports.logMe = function (item) {
  const len = parseInt(arguments.length);
  for (let i = 0; i < len; i++) {
    console.log(i + ': ' + arguments[i]);
  }
};
