#!/usr/bin/node
const arg1 = Number(process.argv[2]);
function mul (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  }
  return a * mul(a - 1);
}
console.log(mul(arg1));
