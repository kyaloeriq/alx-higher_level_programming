#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node getWedgeMovies.js <api_url>');
  process.exit(1);
}

const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data, status code: ${response.statusCode}`);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    let wedgeCount = 0;

    films.forEach((film) => {
      if (film.characters.includes(wedgeId)) {
        wedgeCount++;
      }
    });

    console.log(wedgeCount);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
