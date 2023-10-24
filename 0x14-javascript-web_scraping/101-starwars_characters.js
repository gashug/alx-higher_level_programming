#!/usr/bin/node

const request = require('request');

const baseURL = 'https://swapi-api.alx-tools.com/api/';

function printStarWarsCharacters(movieId) {
  const filmURL = `${baseURL}films/${movieId}/`;

  request(filmURL, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching movie data');
      return;
    }

    const filmData = JSON.parse(body);

    if (filmData.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    const characterURLs = filmData.characters;
    fetchAndPrintCharacters(characterURLs, 0);
  });
}

function fetchAndPrintCharacters(characterURLs, index) {
  if (index >= characterURLs.length) {
    return;
  }

  request(characterURLs[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      fetchAndPrintCharacters(characterURLs, index + 1);
    } else {
      console.error(`Error fetching character data for character ${index + 1}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

printStarWarsCharacters(movieId);
