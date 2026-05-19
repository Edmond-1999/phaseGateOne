const prompt = require("prompt-sync")();

let score = parseInt(prompt("Enter a score: "));

if(score >= 50){
    console.log("pass");
}
else{
    console.log("fail");
}
