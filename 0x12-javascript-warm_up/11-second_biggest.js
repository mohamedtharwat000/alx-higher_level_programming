#!/usr/bin/node
const args = process.argv;
let max = 0;
for (const arg of args) {
  if (arg > max) {
    max = arg;
  }
}
console.log(max);
