#!/usr/bin/node

const args = process.argv.slice(2);
if (Number(args[0])) {
  for (let i = 1; i <= args[0]; i++) {
    for (let j = 1; j <= args[0]; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
