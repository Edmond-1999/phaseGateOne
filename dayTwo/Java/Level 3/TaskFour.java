import java.util.Scanner;

public class TaskFour{
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = input.nextInt();

        for(int index = 0; index <= 11; index++){
            System.out.println(number + " * " + index + " = " + number*index);
        }
    }
}
