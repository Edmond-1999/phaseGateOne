const prompt = require("prompt-sync")();

let firstNumber = parseInt(prompt("Enter the first number: "));

let secondNumber = parseInt(prompt("Enter the second number: "));

let product = firstNumber * secondNumber;

console.log("The product is " + product);
