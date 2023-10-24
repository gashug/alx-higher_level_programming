#!/usr/bin/node

const request = require('request');

// Define the base URL for the Star Wars API (SWAPI).
const baseURL = 'https://swapi.dev/api/';

// Function to fetch and print character names for a specific movie.
function printStarWarsCharacters(movieId) {
  const filmURL = `${baseURL}films/${movieId}/`;

  // Make an HTTP GET request to retrieve information about the specified movie.
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

    // Fetch character data and print their names.
    const characterURLs = filmData.characters;
    fetchAndPrintCharacters(characterURLs, 0);
  });
}

// Recursive function to fetch and print character names.
function fetchAndPrintCharacters(characterURLs, index) {
  if (index >= characterURLs.length) {
    return;
  }

  request(characterURLs[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);

      // Fetch and print the next character.
      fetchAndPrintCharacters(characterURLs, index + 1);
    } else {
      console.error(`Error fetching character data for character ${index + 1}`);
    }
  });
}

// Check if the Movie ID is provided as a command-line argument.
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Call the main function to start the process.
printStarWarsCharacters(movieId);
