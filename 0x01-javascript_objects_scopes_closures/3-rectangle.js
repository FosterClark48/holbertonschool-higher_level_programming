#!/usr/bin/node

// Create class Rectangle that has width & height attributes
// if w & h are not positive ints, return empty obj
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Create print() method which prints a rectangle w/ the char X
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
