#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];
let content = '';

fs.readFile(fileA, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  content += data;

  fs.readFile(fileB, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading file:', err);
      return;
    }
    content += data;

    fs.appendFile(destinationFile, content, 'utf8', (err) => {
      if (err) {
        console.error('Error appending to file:', err);
        return;
      }
    });
  });
});

