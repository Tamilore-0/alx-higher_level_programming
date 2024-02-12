#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 0; i < process.argv.length; i++) {
    let number = parseInt(process.argv[i]);
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    }
  }
  console.log(secondLargest);
}
