#!/usr/bin/node
let currentNumber = 0;
exports.logMe = function (item) {
  currentNumber++;
  console.log(`${currentNumber}: ${item}`);
};
