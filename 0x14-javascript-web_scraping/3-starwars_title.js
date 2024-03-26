#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 */

if (process.argv.length > 2) {
  const id = process.argv[2];
  const request = require('request');
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    console.log(JSON.parse(body).title);
  });
}
