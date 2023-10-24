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

    fetchAndPrintCharacters(filmData.characters);
  });
}

function fetchAndPrintCharacters(characterURLs) {
  let characterIndex = 0;

  function fetchNextCharacter() {
    if (characterIndex >= characterURLs.length) {
      return;
    }

    request(characterURLs[characterIndex], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);

        characterIndex++;

        fetchNextCharacter();
      } else {
        console.error(`Error fetching character data for character ${characterIndex + 1}`);
      }
    });
  }

  fetchNextCharacter();
}

if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

printStarWarsCharacters(movieId);
