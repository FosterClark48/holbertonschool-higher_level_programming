#!/usr/bin/node
// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json using JQuery API

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(url, function (data) {
    $('#character').text(data.name);
  });
});
