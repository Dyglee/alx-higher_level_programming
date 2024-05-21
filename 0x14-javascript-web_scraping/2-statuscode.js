#!/usr/bin/node
/*
 * This script makes a GET request to a given URL and displays the status code.
 * The first argument is the URL to request (GET).
 * The status code is printed like this: code: <status code>.
 */

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
