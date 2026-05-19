const prompt = require("prompt-sync")();

let firstNumber = parseInt(prompt("Enter the first number: "));

let secondNumber = parseInt(prompt("Enter the second number: "));

let sum = firstNumber + secondNumber;

console.log("The sum is " + sum);
