#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];

if (!path) {
  console.error('Usage: node script.js <file_path>');
  process.exit(1);
}

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error('An error occurred:', err);
    return;
  }
  console.log(data);
});
