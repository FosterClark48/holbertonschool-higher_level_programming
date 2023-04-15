#!/usr/bin/node
// Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  // Select div element using id, add click event listener
  $('#add_item').on('click', function() {
    // Execute this code when click event occurs, turning the header red
    $('UL.my_list').append('<li>Item</li>');
  });
});
