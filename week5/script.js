//array of cars
let cars = [
    { make: "Toyota", model: "Camry", year: 2020 },
    { make: "Honda", model: "Accord", year: 2019 },
    { make: "Ford", model: "Mustang", year: 2021 },
    { make: "Chevrolet", model: "Malibu", year: 2018 }]

//print the array
// console.log(cars);
//print the first car
 // console.log((cars[0].make));

//function take two parameters from input that is name and email address and give output hello my name is and email address is 

function greet(name, email) {
    return "Hello, my name is " + name + " and my email address is " + email;
}
//call the function
let name = "John Doe";
let email = "johndoe@example.com";
console.log(greet(name, email));

//function to add two numbers
function add(num1, num2) {
    return num1 + num2;
}
//call the function
let number1 = 5;
let number2 = 10;
console.log("The sum of " + number1 + " and " + number2 + " is: " + add(number1, number2));


//print the current date and time
let currentDate = new Date();

console.log("Current date and time: " + currentDate);

// lets A=50 and b=20 ,,print modulus of a and b
let a = 50;
let b = 20;
let modulus = a % b;
console.log("The modulus of " + a + " and " + b + " is: " + modulus);

// perform addition
let addition = a + b;
console.log("The addition of " + a + " and " + b + " is: " + addition);
// perform subtraction
let subtraction = a - b;
console.log("The subtraction of " + a + " and " + b + " is: " + subtraction);

// perform multiplication
let multiplication = a * b;
console.log("The multiplication of " + a + " and " + b + " is: " + multiplication);
// perform division
let division = a / b;
console.log("The division of " + a + " and " + b + " is: " + division);
// perform exponentiation
let exponentiation = a ** b;
console.log("The exponentiation of " + a + " and " + b + " is: " + exponentiation);
// perform floor division
let floorDivision = Math.floor(a / b);
console.log("The floor division of " + a + " and " + b + " is: " + floorDivision);

// perform ceil division
let ceilDivision = Math.ceil(a / b);
console.log("The ceil division of " + a + " and " + b + " is: " + ceilDivision);

//comparison operators - used to compare two values and return boolean result (true or false)
// ==, !=, ===, !==, >, <, >=, <
// == : equal to
// != : not equal to
// === : strictly equal to
// !== : strictly not equal to
// > : greater than
// < : less than
let d =100; //integer
let e = '200'; //string
let isEqual = (d == e);
let isNotEqual = (d != e);
let isGreaterThan = (d > e);
let isLessThan = (d < e);
let isGreaterThanOrEqual = (d >= e);
let isLessThanOrEqual = (d <= e);
console.log("Is d equal to e? " + isEqual);
console.log("Is d not equal to e? " + isNotEqual);
console.log("Is d greater than e? " + isGreaterThan);
console.log("Is d less than e? " + isLessThan);
console.log("Is d greater than or equal to e? " + isGreaterThanOrEqual);
console.log("Is d less than or equal to e? " + isLessThanOrEqual);


//logical operators - used to combine two or more boolean expressions and return boolean result (true or false)
// &&, ||, !
// && : logical AND
// || : logical OR
// ! : logical NOT

let myAge = 25;
let isLearner = true;

//use comaprison and logical operators if age is less than 25 and is learner
let isEligible = (myAge < 25 && isLearner);
console.log("Is the person learner? " + isEligible);

