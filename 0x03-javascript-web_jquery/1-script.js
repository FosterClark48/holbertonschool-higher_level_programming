#!/usr/bin/node
// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) using JQuery API.

// Ensure that the script will only run after the DOM has fully loaded.
$(document).ready(function () {
  $('header').css('color', '#FF0000');
});
