#!/usr/bin/node

// convert CL args 2 & 3 to integers in base 10
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

// Create function that adds args a & b
function add (a, b) {
  return a + b;
}

// Print result
console.log(add(a, b));
