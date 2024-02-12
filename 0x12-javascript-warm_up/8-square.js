#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);

  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
