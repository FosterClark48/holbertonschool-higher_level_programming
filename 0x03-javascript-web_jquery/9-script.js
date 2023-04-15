#!/usr/bin/node
// Write a JavaScript script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello using JQuery API
// The translation of “hello” must be displayed in the HTML tag DIV#hello
// Your script must work when it is imported from the <head> tag

// Use window.onload instead of $(document).ready() so the script will only execute after all external resources, including the jQuery library, are fully loaded
// ensuring that it works properly when imported from the <head> tag
window.onload = function () {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.getJSON(url, function (data) {
    $('#hello').text(data.hello);
  });
};
