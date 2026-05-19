const prompt = require("prompt-sync")();

let celsius = parseInt(prompt("Enter the temperature in celsius: "));

let fahrenheit = (celsius * (9 / 5)) + 32;

console.log(celsius + " in fahrenheit is " + fahrenheit);
