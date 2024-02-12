#!/usr/bin/node

if (process.argv.length < 4) {
  const num = 0
  console.log(num);
} else {
  let largest = 0;
  let secondLargest = 0;
  for (let i = 0; i < process.argv.length; i++) {
    const number = parseInt(process.argv[i]);
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    }
  }
  console.log(secondLargest);
}
