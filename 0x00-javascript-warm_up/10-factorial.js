#!/usr/bin/node

// Use destructuring assignment to extract third element from CL args
const [, , n] = process.argv;

// Convert n to int in base 10 and store in input variable
const input = parseInt(n, 10);

// Create factorial function that takes one arg 'n'
// if 'n' is Not a Number or 'n' is less than or equal to 1, return 1
// if 'n' is greater than 1 and is a number, compute factorial recursively
// e.g. n = 5: 5 * factorial(4) and so on until it reaches 1
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Call factorial function with parsed input and print result
console.log(factorial(input));
