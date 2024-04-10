#!/usr/bin/node

// Access the first argument passed to the script
const firstArg = process.argv[2];

// Look out for the first command-line argument
if (firstArg) {
  console.log(`${firstArg}`);
} else {
  console.log('No argument');
}
