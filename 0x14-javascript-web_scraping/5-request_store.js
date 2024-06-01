#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function fetchAndSaveWebpage(url, filePath) {
  request(url, { encoding: 'utf8' }, (error, response, body) => {
    if (error) {
      console.error('Error fetching the webpage:', error);
      return;
    }

    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
          console.error('Error writing to file:', err);
          return;
        }
        console.log(`Webpage content successfully saved to ${filePath}`);
      });
    } else {
      console.log(`Failed to fetch the webpage. Status code: ${response.statusCode}`);
    }
  });
}

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Usage: node script.js <url> <file_path>');
  process.exit(1);
}

fetchAndSaveWebpage(url, filePath);
