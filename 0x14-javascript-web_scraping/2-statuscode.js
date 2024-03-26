#!/usr/bin/node

if (process.argv.length > 2) {
  const request = require('request');
  const url = process.argv[2];
  // Making a GET request
  request(url, (error, response) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    console.log('code:', response.statusCode);
  });
}
