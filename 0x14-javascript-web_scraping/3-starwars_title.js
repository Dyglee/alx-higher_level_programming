#!/usr/bin/node
/*
 * This script fetches and prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID.
 * The Star Wars API endpoint is https://swapi-api.alx-tools.com/api/films/:id.
 */

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
