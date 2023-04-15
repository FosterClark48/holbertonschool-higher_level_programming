#!/usr/bin/node
// Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  // Select div element using id, add click event listener
  $('#update_header').on('click', function() {
    // Execute this code when click event occurs, turning the header red
    $('header').text('New Header!!!');
  });
});
