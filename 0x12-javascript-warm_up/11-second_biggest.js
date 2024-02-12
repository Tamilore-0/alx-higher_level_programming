#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > largest) {
      secondLargest = largest;
      largest = process.argv[i];
    }
  }
  console.log(secondLargest);
}
