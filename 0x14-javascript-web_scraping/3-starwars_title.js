#!/usr/bin/node

const request = require('request');

// Check if the Movie ID is provided as a command-line argument.
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Define the base URL for the Star Wars API.
const baseURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to retrieve information about the specified movie.
request(baseURL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error('Error fetching movie data');
  }
});
