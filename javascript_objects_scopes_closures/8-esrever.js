#!/usr/bin/node
exports.esrever = function (list) {
  const my_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    my_list.push(list[i]);
  }
};
