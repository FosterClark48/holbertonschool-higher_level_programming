#!/usr/bin/node
// script that writes a string to a file.

// Import fs module which provides an API to interact w/ the file system
const fs = require('fs');

// Get CL args after first 2 args which are node executable path (node) & script file path (script.js)
const args = process.argv.slice(2);

// Check if there are enough args
if (args.length < 2) {
  console.error('Usage: ./script.js <file_path> <string_to_write>');
  process.exit(1);
}

// Extract file path & string to write args
const filePath = args[0];
const stringToWrite = args[1];

// Write string to file
fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    // If error occurred, print error object
    console.error(error);
  }
});
