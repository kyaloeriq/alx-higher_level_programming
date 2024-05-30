#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

if (!path) {
  console.error('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

// If content is undefined, set it to an empty string
const contentToWrite = content || '';

fs.writeFile(path, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
