const prompt = require("prompt-sync")();

let radius = parseInt(prompt("Enter the radius: "));

let circumference = 2 * 3.142 * radius;

console.log("The circumference is " + circumference);
