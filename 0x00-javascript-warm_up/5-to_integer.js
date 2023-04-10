#!/usr/bin/node

// Extract the first arg passed (at index 2) and store in input var
const input = process.argv[2];
// Convert input value into an int. First value is input, second value is base
const integer = parseInt(input, 10);

// Check if value is an int, if so, print message, if not, print other message
if (Number.isInteger(integer)) {
    console.log(`My number: ${integer}`);
} else {
    console.log("Not a number");
}
