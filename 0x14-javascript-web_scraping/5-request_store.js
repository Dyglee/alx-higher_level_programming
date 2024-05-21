#!/usr/bin/node
/*
 * This script gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request.
 * The second argument is the file path to store the body response.
 * The file must be UTF-8 encoded.
 */

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
