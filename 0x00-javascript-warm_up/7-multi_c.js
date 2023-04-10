#!/usr/bin/node

const args = process.argv.slice(2);

// if args = 0 or is Not a Number, print message
if (args.length === 0 || isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurences')
} else {
  let x = parseInt(args[0]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
