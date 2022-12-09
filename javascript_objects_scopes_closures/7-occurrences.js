#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  var c = 0;
  for (const i in list) {
    if (i === searchElement) {
      c += 1;
    }
  }
  return c;
};
