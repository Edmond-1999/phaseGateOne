const prompt = require("prompt-sync")();

let length = parseInt(prompt("Enter the length: "));

let width = parseInt(prompt("Enter the width: "));

let area = length * width;

console.log("The area is " + area);
