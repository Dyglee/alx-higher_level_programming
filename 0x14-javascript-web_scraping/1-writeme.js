#!/usr/bin/node

/*
 * This script writes a string to a file.
 * The first argument is the file path.
 * The second argument is the string to write.
 * The content of the file is written in utf-8.
 * If an error occurs during writing, it prints the error object.
 */

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

if (!filePath || !fileContent) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
