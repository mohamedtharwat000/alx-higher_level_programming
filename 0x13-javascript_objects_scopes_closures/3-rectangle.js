#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (x) {
    for (let i = 0; i < x; i++) {
      console.log('X'.repeat(x));
    }
  }
}
module.exports = Rectangle;
