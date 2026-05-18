import java.util.Scanner;
import java.util.Random;

public class NumberGuesserApp{
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);
        Random random = new Random();

        int counter = 0;

        int guessedNumber;

        int randomNumber = random.nextInt(1, 101);


        while(true){
            if(counter == 6){
                break;
            }

            System.out.print("Enter your guess(between 1 and 100): ");
            guessedNumber = input.nextInt();
            if(randomNumber == guessedNumber){
                counter++;
                System.out.println("You Guessed Correctly");
                break;
            }
            else if(randomNumber < guessedNumber){
                System.out.println("Too High Try Again");
                if(guessedNumber > 100){
                System.out.println("Please let your number be between 1 and 100");
                }
                else{
                    counter++;
                }

            }
            else if(randomNumber > guessedNumber){
                System.out.println("Too Low Try Again");
                if(guessedNumber < 1){
                System.out.println("Please let your number be between 1 and 100");
                }
                else{
                    counter++;
                }

            }

        }

    System.out.println();


    if(counter == 1){
        System.out.println("Lengendary");
    }
    else if(counter == 2){
        System.out.println("Excellent");
    }
    else if(counter == 3){
        System.out.println("Good");
    }
    else if(counter == 4){
        System.out.println("Good");
    }
    else if(counter == 5){
        System.out.println("Close!");
    }
    else{
        System.out.println("Better Luck");
    }


    System.out.println("You attempted " + counter + " times.");
    System.out.println("The correct number is " + randomNumber);

    }
}
