#!/usr/bin/node
/*
 * This script prints the number of movies where the character "Wedge Antilles" is present.
 * The first argument is the API URL of the Star Wars API.
 * Wedge Antilles is character ID 18 - the script uses this ID for filtering the result of the API.
 */

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
