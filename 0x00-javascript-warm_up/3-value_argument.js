#!/usr/bin/node

// Get CL args, excluding first two element (node & script path)
const args = process.argv.slice(2);

// Check if first arg exists and print it, otherwise print 'No argument'
if (args[0] !== undefined) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
