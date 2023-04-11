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

  // Create rotate() method which exchanges the width & height of rectangle
  rotate () {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  // Create double() method which multiplies the width & height by 2
  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
