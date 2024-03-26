#!/usr/bin/node
/**
 * Description: This script writes a string to a file.
 */
if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const string = process.argv[3];

  const fs = require('fs');

  // writing to a file
  fs.writeFile(filePath, string, 'utf8', (err) => {
    if (err) {
      console.error('Error reading file:', err);
    }
  });
}
