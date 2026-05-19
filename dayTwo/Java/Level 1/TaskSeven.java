import java.util.Scanner;

public class TaskSix{
    public static void main(String[] args){
        
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the radius of the circle: ");
        int radius = input.nextInt();

        double circumference = 2 * 3.142 * radius;

        System.out.println("The circumference is " + circumference);
    }
}
