#!/usr/bin/node
const request = require('request');

function getStarWarsMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode === 200) {
      console.log(`The title of the Star Wars movie with episode number ${movieId} is '${body.title}'.`);
    } else {
      console.log(`No movie found with episode number ${movieId}.`);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieIdInt = parseInt(movieId);

if (isNaN(movieIdInt)) {
  console.log('The movie ID must be an integer.');
  process.exit(1);
}

getStarWarsMovieTitle(movieIdInt);
