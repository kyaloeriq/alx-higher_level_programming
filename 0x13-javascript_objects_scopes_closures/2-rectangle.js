#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
   if (w >= 0 && h >= 0) {
     this.width = w;
     this.height = h;
   } else {
     // If either width or height is negative, set both to 0
     this.width = 0;
     this.height = 0;
   }
 }
}

module.exports = Rectangle;
