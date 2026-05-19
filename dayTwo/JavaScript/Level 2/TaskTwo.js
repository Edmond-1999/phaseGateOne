const prompt = require("prompt-sync")();

let number = parseInt(prompt("Enter a number: "));

if(number > 0){
    console.log("positive");
}
else if(number < 0){
    console.log("negative");
}
