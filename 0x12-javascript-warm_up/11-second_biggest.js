#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
  process.exit();
}
let max = args[0];
for (const arg of args) {
  if (Number(arg) > max) {
    max = Number(arg);
  }
}
console.log(max);
