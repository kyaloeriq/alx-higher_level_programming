#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
   if (w !== undefined && h !== undefined && Number.isInteger(w) && Number.isInteger(h) && w > 0 && h > 0) {
     this.width = w;
     this.height = h;
   } else {
     // If w or h is equal to 0 or not a positive integer, create an empty object
   }
 }
}

module.exports = Rectangle;
