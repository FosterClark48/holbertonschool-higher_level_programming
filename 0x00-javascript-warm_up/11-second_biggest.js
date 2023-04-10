#!/usr/bin/node

// Extract CL args and change to int
// First 2 elements are path to Node.js executable and path to script file, use slice(2) to remove them
// Use map(Number) to convert remaining args to integers
const args = process.argv.slice(2).map(Number);
// Create new array 'uniqueArgs' containing unique elements of 'args' array by removing duplicates using new Set object
// Convert new Set object back into array using spread syntax (...)
const uniqueArgs = [...new Set(args)];

// if uniqueArgs array (non-dup CL args) is less than 1, print 0
// if its more than 1, proceed to find second largest int
if (uniqueArgs <= 1) {
  console.log(0);
} else {
  // Sort uniqueArgs array in ascending numerical order
  //
  uniqueArgs.sort((a, b) => a - b);
  console.log(uniqueArgs[uniqueArgs.length - 2]);
}
