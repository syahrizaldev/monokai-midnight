// 1. Example
let firstName = 'John';
let lastName = 'Marteen';

console.log(`Hello my name is ${firstName} ${lastName}.`);

let Sales = 'Toyota';

function CarTypes(name) {
   if (name == 'Honda') {
      return name;
   } else {
      return "Sorry, we don't sell " + name + '.';
   }
}

let car = { myCar: 'Saturn', getCar: CarTypes('Honda'), special: Sales };
console.log(car.special);

class Product {
   constructor(name, price) {
      this.name = name;
      this.price = price;

      if (price < 0) {
         throw RangeError('Cannot create product ' + this.name + ' with a negative price');
      }
   }
}

class Food {
   constructor(name, price) {
      Product.call(this, name, price);
      this.category = 'food';
   }
}

class Toy {
   constructor(name, price) {
      Product.call(this, name, price);
      this.category = 'toy';
   }
}

let cheese = new Food('feta', 5);
let fun = new Toy('robot', 40);

