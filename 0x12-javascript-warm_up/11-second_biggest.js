#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
  process.exit();
}
args.sort((a, b) => a - b);
args.pop();
console.log(args.pop());
