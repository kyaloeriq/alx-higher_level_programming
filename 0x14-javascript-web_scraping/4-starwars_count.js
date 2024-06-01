#!/usr/bin/node
const request = require('request');

const countMoviesWithWedge = (apiUrl) => {
  request(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error fetching data from API: ${error}`);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`Unexpected response status: ${response.statusCode}`);
      return;
    }

    const films = body.results;
    const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(wedgeId)) {
        count += 1;
      }
    });

    console.log(`${count}`);
  });
};

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Usage: node script.js <API_URL>');
  process.exit(1);
}

countMoviesWithWedge(apiUrl);
