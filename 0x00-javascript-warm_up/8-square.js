#!/usr/bin/node

// define printSquare function which takes single arg 'size'
// for loop prints 'size' number of rows, each row contains 'size' number of 'X' chars
function printSquare (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}

// Parse CL args - [0] is node, [1] is file, [2] is arg we want
const [, , sizeArg] = process.argv;
// convert size arg to an int w/ 10 base and store in 'size' variable
const size = parseInt(sizeArg, 10);

// if size arg is Not a Number, print message, otherwise print X size times
if (isNaN(size)) {
  console.log('Missing size');
} else {
  printSquare(size);
}
