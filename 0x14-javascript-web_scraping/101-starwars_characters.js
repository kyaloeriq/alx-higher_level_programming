#!/usr/bin/node
const request = require('request');

function fetchCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error('Failed to fetch data from the API'));
        return;
      }
      resolve(JSON.parse(body).name);
    });
  });
}

function printCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, async (error, response, body) => {
    if (error) {
      console.error('Failed to fetch data from the API:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch data from the API:', body);
      return;
    }

    const film = JSON.parse(body);
    const characters = film.characters;

    for (const characterUrl of characters) {
      try {
        const name = await fetchCharacterName(characterUrl);
        console.log(name);
      } catch (err) {
        console.error('Failed to fetch character name:', err);
      }
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

printCharacters(movieId);

