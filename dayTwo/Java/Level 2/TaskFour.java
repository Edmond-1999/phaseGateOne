import java.util.Scanner;

public class TaskFour{
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int firstNumber = input.nextInt();

        System.out.print("Enter a number again: ");
        int secondNumber = input.nextInt();

        if(firstNumber > secondNumber){
            System.out.println(firstNumber + " is the largest");
        }
        else if(secondNumber > firstNumber){
            System.out.println(secondNumber + " is the largest");
        }
    }
}
