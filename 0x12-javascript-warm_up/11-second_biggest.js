#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log('0');
} else {
  let largest = parseInt(args[0], 10);
  let secondLargest = parseInt(args[1], 10);

  if (secondLargest > largest) {
    [largest, secondLargest] = [secondLargest, largest];
  }

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i], 10);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  console.log(secondLargest);
}
