#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
   if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
     this.width = w;
     this.height = h;
   } else {
     // If either width or height is negative, set both to 0
     this.width = undefined;
     this.height = undefined; 
   }
 }
}

module.exports = Rectangle;
