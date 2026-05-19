const prompt = require("prompt-sync")();

let firstNumber = parseInt(prompt("Enter a number: "));

let secondNumber = parseInt(prompt("Enter a number again: "));

if(firstNumber > secondNumber){
    console.log(firstNumber + " is the largest")
}
else if(secondNumber > firstNumber){
    console.log(secondNumber + " is the largest")
}
