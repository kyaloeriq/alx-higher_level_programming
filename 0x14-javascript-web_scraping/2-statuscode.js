#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Usage: node statusCode.js <URL>');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
