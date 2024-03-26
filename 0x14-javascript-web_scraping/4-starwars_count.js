#!/usr/bin/node

/**
 * script that prints the number of movies
 * where the character “Wedge Antilles” is present.
 */

if (process.argv.length > 2) {
  const url = process.argv[2];
  const request = require('request');

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const jsonData = JSON.parse(body);

    let count = 0;

    for (let i = 0; i < Object.entries(jsonData).length; i++) {
      jsonData.results[i].characters.forEach(string => {
        if (string.endsWith('18/')) {
          count += 1;
        }
      });
    }
    console.log(count);
  });
}
