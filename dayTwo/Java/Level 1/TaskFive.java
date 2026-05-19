import java.util.Scanner;

public class TaskFive{
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the temperature in celsius: ");
        double celsius = input.nextDouble();


        double fahrenheit = (celsius * 9 / 5) + 32;

        System.out.println(celsius + " in fahrenheit is " + fahrenheit);

    }
}
