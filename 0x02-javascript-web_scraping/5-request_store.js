#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

// Import request and fs modules
const request = require('request');
const fs = require('fs');

// Check if there are enough args
if (process.argv.length < 3) {
  console.error('Usage: ./5-request_store.js <URL> <output_file_path>');
  process.exit(1);
}

// Get URL from CL arg
const url = process.argv[2];
const filePath = process.argv[3];

// Make GET request and print status code
// .get() takes 2 args: URL and callback function
// callback function takes 2 args: error object and response object
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) {
      // If error occurred, print error object
      console.error(error);
    }
  });
});
