#!/usr/bin/node
const args = process.argv;
if (args[2]) {
  console.log(args[2]);
  process.exit();
}
console.log('No argument');
