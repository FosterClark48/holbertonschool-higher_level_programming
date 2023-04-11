#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Create class Square that inherits from Rectangle from 4-rectangle.js that has size attribute
// Call constructor of Rectangle using super() to initialize width & height attributes w/ value of 'size'
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
