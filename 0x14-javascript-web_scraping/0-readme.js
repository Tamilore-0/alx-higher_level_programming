#!/usr/bin/node

if (process.argv.length > 2) {
  const filePath = process.argv[2];

  const fs = require('fs');

  // Reading from a file
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }
    process.stdout.write(data);
  });
}
