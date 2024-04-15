#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
   if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
     this.width = w;
     this.height = h;
   } else {
     // If w or h is equal to 0 or not a positive integer, create an empty object
     return {};
   }
 }
}

module.exports = Rectangle;
