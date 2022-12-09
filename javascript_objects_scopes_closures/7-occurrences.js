#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const i in list) {
    if (i === searchElement) {
      c += 1;
    }
  }
  return c;
};
