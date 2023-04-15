#!/usr/bin/node
// script that updates the text color of the <header> element to red (#FF0000)

// Ensure that the script waits for the DOM to fully load before manipulating <header> element
document.addEventListener('DOMContentLoaded', function() {
  let header = document.querySelector("header");
  header.style.color = '#FF0000';
});
