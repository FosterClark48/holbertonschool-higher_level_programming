#!/usr/bin/node
// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000)
// when the user clicks on the tag DIV#red_header using JQuery API.

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  // Select div element using id, add click event listener
  $('#red_header').on('click', function() {
    // Execute this code when click event occurs, turning the header red
    $('header').css('color', '#FF0000');
  });
});
