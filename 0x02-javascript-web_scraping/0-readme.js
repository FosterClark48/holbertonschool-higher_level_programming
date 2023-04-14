#!/usr/bin/node
// script that reads and prints the content of a file.

// Import fs module which provides an API to interact w/ the file system
const fs = require('fs');

// Check if file path argument is provided
if (process.argv.length < 3) {
  console.error('Usage: ./script.js <file_path>');
  process.exit(1);
}

// Read file using fs (file system)
// readFile() method args - 1. file path 2. encoding 3. callback function
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
