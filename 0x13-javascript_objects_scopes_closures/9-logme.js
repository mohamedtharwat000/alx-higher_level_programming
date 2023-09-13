#!/usr/bin/node
let currentNumber = 0;
exports.logMe = function (item) {
  console.log(`${currentNumber}: ${item}`);
  currentNumber++;
};
