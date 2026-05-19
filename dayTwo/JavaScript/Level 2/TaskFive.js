const prompt = require("prompt-sync")();

let firstNumber = parseInt(prompt("Enter a number: "));

let secondNumber = parseInt(prompt("Enter a number again: "));

let thirdNumber = parseInt(prompt("Enter another number again: "));

let largest = firstNumber;

if(secondNumber > largest){
    largest = secondNumber;
}
if(thirdNumber > largest){
    largest = thirdNumber;
}


console.log(largest);
