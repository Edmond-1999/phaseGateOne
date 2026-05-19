import java.util.Scanner;

public class TaskTwo{
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.print("What is your age: ");
        int age = input.nextInt();

        System.out.println("In five years you will be " + (age + 5));

    }
}
