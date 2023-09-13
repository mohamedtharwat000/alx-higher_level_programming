#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    const char = c ?? 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
