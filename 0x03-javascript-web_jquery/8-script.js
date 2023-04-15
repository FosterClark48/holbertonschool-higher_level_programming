#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json using JQuery API
// All movie titles must be list in the HTML tag UL#list_movies

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(url, function (data) {
    const movies = data.results;
    for (let i = 0; i < movies.length; i++) {
      $('UL#list_movies').append(`<li>${movies[i].title}</li>`);
    }
  });
});
