#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

// Import request module which is used to make HTTP requests
const request = require('request');

// Get the API URL from the first command line argument (process.argv[2]) and assign it to a variable api_url
const apiURL = process.argv[2];
const wedgeID = 18;

// Make a GET request to the apiURL using request with a callback function that handles the response
request(apiURL, (error, response, body) => {
  if (!error) {
    // Parse JSON response recieved in the body variable. .results property of parsed object is an array of movies
    const movies = JSON.parse(body).results;
    // movies.filter() iterates over the movies array & returns a new array containing only the movies where Wedge Antilles is present
    // filter() method takes a callback function as an argument, which is invoked once for each element in the array.
    // The arrow function takes one argument, movie, which represents the current element being processed in the movies array.
    // The includes() function checks if the characters property of the movie object includes the URL for Wedge Antilles.
    // It checks if the specified value (the URL for Wedge Antilles) is present in the array
    // After the filter() function is done iterating over the movies array, it returns a new array containing only the movies where the condition in the arrow function is true.
    // By calling the .length property on the array it gives us the count of movies featuring Wedge Antilles.
    const numMoviesWithWedge = movies.filter(movie => movie.characters.includes(`http://swapi.co/api/people/${wedgeID}/`)).length;
    const numMoviesWithWedge2 = movies.filter(movie => movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeID}/`)).length;
    const largerOutput = Math.max(numMoviesWithWedge, numMoviesWithWedge2);
    console.log(largerOutput);
  }
});
