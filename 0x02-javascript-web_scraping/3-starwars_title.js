#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.

// Import request module which is used to make HTTP requests
const request = require('request');
// Store second arg 'movie ID' into movieID variable
const movieID = process.argv[2];

// Check if movieID was provided, if not, print error message
if (!movieID) {
  console.error('Please provide movie ID as an argument');
  process.exit(1);
}

// Store URL w/ movie ID in url variable
const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;

// Create request of star wars API to grab movie title
request(url, (error, response, body) => {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
