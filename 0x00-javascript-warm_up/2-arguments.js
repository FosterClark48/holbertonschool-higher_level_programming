#!/usr/bin/node

// Get CL args, excluding first two element (node & script path)
const args = process.argv.slice(2);

// Check the number of args and print related message
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
