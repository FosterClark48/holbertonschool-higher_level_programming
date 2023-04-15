#!/usr/bin/node
// Write a JavaScript script that adds the class red to the <header> element
// when the user clicks on the tag DIV#red_header using JQuery API.

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  // Select div element using id, add click event listener
  $('#toggle_header').on('click', function() {
    // Execute this code when click event occurs, turning the header red
    // if header has red class, remove and add green, vice versa
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    }
  });
});
