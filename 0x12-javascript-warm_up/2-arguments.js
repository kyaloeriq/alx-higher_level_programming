#!/usr/bin/node

const argv = process.argv.length;

// Check the number of command-line arguments
if (argv === 2) {
  console.log('No argument');
} else if (argv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
