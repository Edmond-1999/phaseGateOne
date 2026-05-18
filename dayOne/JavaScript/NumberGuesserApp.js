const prompt = require("prompt-sync")();

const randomNumber = Math.floor(Math.random() * 101);

let guessedNumber;

let counter = 1;

while(true){
    if(counter == 6){
        break;
    }
    guessedNumber = parseInt(prompt("Enter your guess(between 1 and 100): "));
    if(randomNumber == guessedNumber){
        counter++;
        console.log("You Guessed Correctly");
        break;
    }
    else if(randomNumber < guessedNumber){
        console.log("Too High Try Again");
        if(guessedNumber > 100){
        console.log("Please let your number be between 1 and 100");
        }
        else{
            counter++;
        }

    }
    else if(randomNumber > guessedNumber){
        console.log("Too Low Try Again");
        if(guessedNumber < 1){
        console.log("Please let your number be between 1 and 100");
        }
        else{
            counter++;
        }

    }


}

console.log();


if(counter == 1){
    console.log("Lengendary");
}
else if(counter == 2){
    console.log("Excellent");
}
else if(counter == 3){
    console.log("Good");
}
else if(counter == 4){
    console.log("Good");
}
else if(counter == 5){
    console.log("Close!");
}
else{
    console.log("Better Luck");
}


console.log("You attempted " + counter + " times.");
console.log("The correct number is " + randomNumber);
