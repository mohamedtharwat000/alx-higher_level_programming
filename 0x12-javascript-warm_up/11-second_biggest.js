#!/usr/bin/node
const args = process.argv;
let max = 0;
if (args.length <= 3) {
  console.log(max);
  process.exit();
}
for (const arg of args) {
  if (arg > max) {
    max = arg;
  }
}
console.log(max);
