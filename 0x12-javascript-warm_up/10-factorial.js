#!/usr/bin/node

const args = process.argv.slice(2);
const newVar = Number(args[0]);
const firstArr = [];
let ctr = 1;

for (let i = newVar; i > 0; i--) {
  firstArr.push(i);
}

for (let j = 0; j < firstArr.length; j++) {
  ctr = ctr * firstArr[j];
}
console.log(ctr);
