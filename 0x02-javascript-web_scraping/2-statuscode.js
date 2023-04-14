#!/usr/bin/node
//  script that display the status code of a GET request.

// Import request module which is used to make HTTP requests
const request = require('request');

// Check if there are enough args
if (process.argv.length < 2) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Get URL from CL arg
const url = process.argv[2];

// Make GET request and print status code
// .get() takes 2 args: URL and callback function
// callback function takes 2 args: error object and response object
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
