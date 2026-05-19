public class LevelFour{
    public static int addTwoNumbers(int firstNumber, int secondNumber){
        int sum = firstNumber + secondNumber;
        return sum;
    }

    public static String evenNumberChecker(int number){
        if(number % 2 == 0){
            return "Even";
        }
        else{
            return "Odd";
        }
    }

    public static int squareOfNumber(int number){
        int squared = number * number;
        return squared;
    }

    public static double temperatureConverter(double celsius){
        double fahrenheit = (celsius * 9/5) + 32;
        return fahrenheit;
    }

    public static String primeNumberChecker(int number){
        for(int index = 2; index < number; index++){
            if(number % index != 0){
                return "Prime";
            }

        }
          return "Not prime";

    }

    public static int largestOfThree(int firstNumber, int secondNumber, int thirdNumber){
        int largest = firstNumber;
        if(secondNumber > largest){
            largest = secondNumber;
        }
        if(thirdNumber > largest){
            largest = thirdNumber;
        }

        return largest;
    }

    public static double simpleInterest(double principal, double rate, int time){
        double simpleInterest = (principal * rate/100 * time);
        return simpleInterest;
    }

    public static int areaOfRectangle(int length, int width){
        int area = length * width;
        return area;
    }

    public static int reverseOfNumber(int number){
        int numberLength = StringValueOf(number).length;
        int reversed;
        int remainder;

        for(int index = 1; index < numberLength; index++){
            remainder = number % 10;
            number /= 10;
            reversed *= remainder * 10;
        }
        return reversed;

    }

    public static void main(String[] args){

        System.out.println(addTwoNumbers(1,4));
        System.out.println(evenNumberChecker(4));
        System.out.println(squareOfNumber(5));
        System.out.println(temperatureConverter(16));
        System.out.println(primeNumberChecker(6));
        System.out.println(largestOfThree(2, 5, 4));
        System.out.println(simpleInterest(10000, 17, 7));
        System.out.println(areaOfRectangle(10,6));
        System.out.println(reverseOfNumber(12345));

    }

}
