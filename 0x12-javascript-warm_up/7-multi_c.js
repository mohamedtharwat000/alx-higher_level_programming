#!/usr/bin/node
const arg2 = process.argv[2];
if (isNaN(arg2)) {
  console.log('Missing number of occurrences');
  process.exit();
}
for (let i = 0; i < arg2; i++) {
  console.log('C is fun');
}
