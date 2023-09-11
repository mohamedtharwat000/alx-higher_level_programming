#!/usr/bin/node
const arg2 = process.argv[2];
if (isNaN(Number(arg2))) {
  console.log('Missing size');
  process.exit();
}
for (let i = 0; i < arg2; i++) {
  console.log('X'.repeat(arg2));
}
